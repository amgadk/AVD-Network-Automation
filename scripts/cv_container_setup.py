import ssl
import requests
import time
from cvprac.cvp_client import CvpClient

ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings()

cvp_client = CvpClient()
cvp_ip = "10.18.149.11"
cvp_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJkaWQiOjc1NjA4NDk5NzgyMjI5NjkwODQsImRzbiI6ImF2ZCIsImRzdCI6ImFjY291bnQiLCJleHAiOjE3NjE2MDk3NzcsImlhdCI6MTc2MDQwMDE4Mywib2dpIjozLCJvZ24iOiJEZWZhdWx0Iiwic2lkIjoiMGI5Yzg2MDZiNmU2MDM0OWUxZTliMjZmM2IwODJmNjI3ZWEwOTRmNzU0YzgzM2YxM2MzYzNhYzA2ZTAyNDU5My15b2M5Tkc4N1VlY25IcW5lbk40YnF4SmxmSE8yMHR2VWp3X1haa2tmIn0.mMmjDjJwhHMctnBkbOMhbGrANyAxNV1c0dd5hoQeqs-BHOfYOkSIt-HsfxdHoUJ-HpVY5W6QeQrKJeqioM4CKelU8xmPob89e8DFp06S2-XCpAUkhTOIKlPl7_MrLNCzx2hyK4iCWQ-yGHksWok7TzEN20XD6M1qZZoGuELzopiUpjh5kjb5bzX2PIMbY5LzsB-mQFNhZ49nlqVANU3OynzrRq9unClj0EQoIROZiruiGeSz_VGSXSiTqTFkoQORG_cbt-NrcQVm3mt5znjbP-pCOvih7csESheL5ph7tRalj6ps7xFVdfXb3QFvngjBRlUT7DZm5Xm5k09mU8f7LKsIfOATm37XZZ2tXkCpvft1B_S7C6M3VOsFoS572SNZzAIOsduQn2FBcnT3r0hD-LQbyrB2JQuoopgkN416IuxxfKf_SpcqJtrGjfWcFzkIY2AdxZwgtd34g53RSK-iCJfuZdW1wXov0LDpOoSDL4S3rycrJ_2yGzjIC4HyO9UEzuBBSA2ETeagwVx3R167P0AL1pQ0tssI3rH96_uH-fQoXwBGRwlHlIqlt7J_mbTZcTawAPrEc-dD6ZW5iETXahzZ3YHMI_duKjNNRKpsU0n9EZSAJpItWkhs4RfQEJBZlYh58H_b0FqTgZlpz_LE-Ufg7sBRnSS0TTG4huDHpBU"



def cvp_connection():
    """
    Connect to CloudVision instance.

    Parameters:
    self (object): The instance of the class.

    self.cvp_ip (str): The IP address of the CloudVision instance.
    self.is_cvaas (bool): A flag indicating whether the CloudVision instance is a Cloud Vision as a Service (CVAAS) instance.
    self.cvp_token (str): The API token for authentication with the CloudVision instance.

    Returns:
    None. The function establishes a connection to the CloudVision instance.
    """
    cvp_client.connect(
        nodes=[cvp_ip],
        username="",
        password="",
        api_token=cvp_token,
    )

def cvp_move_devices():
    """
    This function moves devices from the 'Undefined' container to the 'Tenant' container in CVP.

    Parameters:
    None

    Returns:
    None
    """
    cvp_connection()

    device_list = [
        {"deviceName": device["fqdn"]}
        for device in cvp_client.api.get_devices_in_container("Undefined")
    ]

    for device in device_list:
        device_info = cvp_client.api.get_device_by_name(
            device["deviceName"]
        )
        new_container = cvp_client.api.get_container_by_name("Tenant")
        cvp_client.api.move_device_to_container(
            "python", device_info, new_container
        )

    cvp_execute_pending_tasks()


def cvp_create_configlets():
    """
    This function creates and applies configlets to devices in the 'Tenant' container.

    Parameters:
    None

    Returns:
    None
    """
    time.sleep(20)
    print("Waiting for 20 seconds")
    cvp_connection()

    device_list = cvp_client.api.get_devices_in_container("Tenant")
    device_info = [
        {"name": device["fqdn"], "macAddress": device["systemMacAddress"]}
        for device in device_list
    ]

    for info in device_info:
        device_mac = info["macAddress"]
        device_short_name = info["name"]
        dev_mgmt = f"{device_short_name}_management"

        get_config = cvp_client.api.get_device_configuration(
            device_mac
        )
        cvp_client.api.add_configlet(dev_mgmt, get_config)

        device_name = cvp_client.api.get_device_by_name(
            device_short_name
        )
        mgmt_configlet = cvp_client.api.get_configlet_by_name(dev_mgmt)
        mgmt_configlet_key = [
            {"name": mgmt_configlet["name"], "key": mgmt_configlet["key"]}
        ]

        cvp_client.api.apply_configlets_to_device(
            "Management Configs", device_name, mgmt_configlet_key
        )


    cvp_execute_pending_tasks()

def cvp_execute_pending_tasks():
    """
    Execute all pending tasks in CVP.

    This function retrieves all pending tasks from CVP using the CVP API and executes each task.

    Parameters:
    None

    Returns:
    None
    """
    tasks = cvp_client.api.get_tasks_by_status("Pending")
    for task in tasks:
        cvp_client.api.execute_task(task["workOrderId"])

cvp_move_devices()
cvp_create_configlets()
