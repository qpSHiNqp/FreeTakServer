#######################################################
# 
# core_name_general_controller.py
# Python implementation of the Class CoreNameGeneralController
# Generated by Enterprise Architect
# Created on:      16-Dec-2022 10:56:05 AM
# Original author: Giu Platania
# 
#######################################################
from digitalpy.core.main.controller import Controller

class COTManagementGeneralController(Controller):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cot_db = COTDatabase()  # initialize COT database object

    def cot_record_in_db(self, cot_record: COTRecord):
        """
        Inserts a new COT record into the database.
        :param cot_record: The COT record to be inserted.
        """
        self.cot_db.insert_cot_record(cot_record)

    def build_drop_point_object(self, cot_record: COTRecord):
        """
        Builds a drop point object from the given COT record.
        :param cot_record: The COT record to be used to build the drop point object.
        :return: The drop point object.
        """
        drop_point = DropPoint()
        drop_point.latitude = cot_record.latitude
        drop_point.longitude = cot_record.longitude
        drop_point.altitude = cot_record.altitude
        return drop_point

    def medevac_send(self, cot_record: COTRecord, drop_point: DropPoint):
        """
        Sends a medevac request with the given COT record and drop point.
        :param cot_record: The COT record to be used in the medevac request.
        :param drop_point: The drop point to be used in the medevac request.
        """
        medevac_request = MedevacRequest(cot_record=cot_record, drop_point=drop_point)
        send_medevac_request(medevac_request)  # send the medevac request

    def medevac_receive(self, medevac_request: MedevacRequest):
        """
        Receives a medevac request and processes it.
        :param medevac_request: The medevac request to be processed.
        """
        cot_record = medevac_request.cot_record
        drop_point = medevac_request.drop_point
        # process the medevac request...
    
    def manage_presence(self, presence_data: dict):
        """Updates the presence information for a specific COT in the system.
        
        Args:
            presence_data (dict): A dictionary containing the updated presence information for the COT.
        """
        # Validate the presence data
        if not self._is_valid_presence_data(presence_data):
            raise InvalidInputError("Invalid presence data provided.")

        # Update the presence information in the database
        self.db.update_cot_presence(presence_data)

    def share_privately(self, cot_id: str, recipient_id: str):
        """Shares a specific COT privately with another user.
        
        Args:
            cot_id (str): The ID of the COT to be shared.
            recipient_id (str): The ID of the user to receive the shared COT.
        """
        # Check if the recipient is a valid user
        if not self.user_manager.is_valid_user(recipient_id):
            raise InvalidInputError("Invalid recipient provided.")

        # Check if the COT exists and is owned by the current user
        cot = self.db.get_cot(cot_id)
        if cot is None or cot.owner_id != self.current_user.id:
            raise InvalidInputError("Invalid COT provided.")

        # Share the COT privately with the recipient
        self.db.add_cot_to_user(cot_id, recipient_id)

    def broadcast(self, cot_id: str):
        """Broadcasts a specific COT to all users in the system.
        
        Args:
            cot_id (str): The ID of the COT to be broadcasted.
        """
        # Check if the COT exists and is owned by the current user
        cot = self.db.get_cot(cot_id)
        if cot is None or cot.owner != self.current_user:
            raise ValueError("Invalid COT ID or unauthorized access.")
        # Create a broadcast message with the COT data
        message = {"type": "cot_broadcast", "cot": cot.to_dict()}
        self.messaging.broadcast(message)

    def cot_broadcast(self):
        # retrieve the COT message from the request values
        cot_message = self.request.get_value("cot_message")
        # broadcast the COT message to all registered listeners
        self.broadcast(cot_message)