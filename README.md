# Automated-Attendance-Using-QR-code
An offline automated attenance using QR code. The logic of the scripts is as follows:

QR Generation
  Import MasterList --> Generate ID-Number --> Append the Generated ID number to the MasterList
  --> Generate QR code Suing the ID-number --> Convert to Binary64 --> Append to MasterList

QR Reader
  Import MasterList (With the ID-NUmber and Binary64 Data) --> QR scann --> Append Date and Time to a copy of MasterList
