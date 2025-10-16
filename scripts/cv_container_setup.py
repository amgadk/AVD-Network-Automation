import ssl
import requests
import time
from cvprac.cvp_client import CvpClient

ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings()

cvp_client = CvpClient()
cvp_ip = "10.18.154.241"
cvp_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJkaWQiOjc1NjE2OTcxNzc3MDE5NzQyNjgsImRzbiI6ImF2ZCIsImRzdCI6ImFjY291bnQiLCJleHAiOjE3NjE4MDY4MTQsImlhdCI6MTc2MDU5NzIxOSwib2dpIjozLCJvZ24iOiJEZWZhdWx0Iiwic2lkIjoiNjA4M2NhZTQ5YjA4MzdjZjg1Mjc3MGJmNDU3ODMyYWZkZGZiYjFkZDRjMWJkZWU4YWVlMjgzMzk0Yjg5MmVhMy1qSmM4RFphRmhEN2hIVmFMbjJEWi1Qamp1RnRFV3I0cGtDdDlpRGtTIn0.PG7DKyXK9K1tBSuJR_UxdVMO66ww0PcLwgkE1LSrfaf3dVTYomimWiECiz2OThJaWy7FjailIhhL5iUrOzEsNx-oDQuBZv0eYhxPLihIIuP6Y9dUy3oAt1WpJ8_mm9h63czWs03C1zpwhXer_MtQ0FTCke8LrBpI_9RzBy24nkqfZPI8aSfv3YGk97MGSfRpBNvOxdpe-V1euJDYEJeZib3YTMwSs9_3k8B0iXP7EUGGNTiZPmh0GUnjFLiJDZO3baHH7Wr9DhZr0IC6q5_Ez96Pf9FHI2J4dQmMGvVMhKrxUNxfr_MW34NowaHtTAVLQ26p49jB81oH0C0FrZx_eSVxWMYivaYRrXlxQGrshFK68Hj5pcZGGgwsqYW9wWVll--1ghn4V9O-JpbCQOavHzTuLdKZyca3FZdgI8F9vKUoaWtOjdQyyA_G4b1f361gmtUMCmEngEolT9VrvxdoH-XQZQmBbY8dFvOlVIQgGj05Ly_ifq1W0yFwoL7yCwGf1IFpbZua8Ey0-3vDeCFBJogM_bQUShC8C-srwejUm6xbADrmpX4w5QxpTpVpXPSQkJfzKHm4kqQg6BEiTr6m1Fye0BXqkOpOQ6cnu_RGL8yhQ_7jIQBcWkW_RpsJ0gCymWm9G4jEhbmOaG5VBvrwdo8u-IUsSUp33xaL4B-4NVE"



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
