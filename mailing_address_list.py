# Created by : Sidney Kang
# Created on : 7 Dec. 2017
# Created for : ICS3UR
# Daily Assignment - Unit 6-05
# This program

from enum import Enum

Provinces = Enum('ON', 'QC', 'NL', 'PE', 'NS', 'NB', 'MB', 'SK', 'AB', 'BC', 'YT', 'NT', 'NU')
Street = Enum('ST', 'DR', 'AVE', 'CRES', 'GRV')

address = []
address.append([])
counter = 0
loop = True

class MailingAddress():
      def __init__(self, last_name, first_name, unit_number, civic_number, street_name, street_type, municipality, province, postal_code):
          self.first_name = first_name
          address[counter].append(self.first_name)
          self.last_name = last_name
          address[counter].append(self.last_name)
          self.unit_number = unit_number
          address[counter].append(self.unit_number)
          self.civic_number = civic_number
          address[counter].append(self.civic_number)
          self.street_name = street_name 
          address[counter].append(self.street_name)                  
          self.street_type = street_type
          address[counter].append(self.street_type)
          self.municipality = municipality  
          address[counter].append(self.municipality)        
          self.province = province
          address[counter].append(self.province)
          self.postal_code = postal_code
          address[counter].append(self.postal_code)                              
        
while loop == True:          
      last_name = raw_input("What is the addressee's last name? ")  
      last_name = last_name.upper()
      first_name = raw_input("What is the addressee's first name? ")  
      first_name = first_name.upper()
      unit_number = raw_input("What is their unit number? ")
      unit_number = unit_number.upper()
      civic_number = raw_input("What is their civic number? ")
      civic_number = civic_number.upper()
      street_name = raw_input("What is the name of the street? ")
      street_name = street_name.upper()    
      street_type = raw_input("What is their street type? ")  
      street_type = street_type.upper()  
      while street_type not in Street:
            street_type = raw_input("Please enter their street type. (ex: Dr) ")     
            street_type = street_type.upper()
      municipality = raw_input("Which municipality is the letter being sent to? ")
      municipality = municipality.upper()
      province = raw_input("Which province is the letter being sent to? ")     
      province = province.upper() 
      while province not in Provinces:
            province = raw_input("Please enter province in abbreviation form (On).")
            province = province.upper()
      province = province
      province = province.upper()      
      postal_code = raw_input("What is their postal code? ")
      postal_code = postal_code.upper()

      mailing_address = MailingAddress(last_name, first_name, unit_number, civic_number, street_name, street_type, municipality, province, postal_code)
      
      address.append([])
      counter = counter + 1
      print (address)
      print(mailing_address.first_name + ' ' + mailing_address.last_name)
      print(mailing_address.unit_number + '-' + mailing_address.civic_number + ' ' + mailing_address.street_name + ' ' + mailing_address.street_type)
      print(mailing_address.municipality + ' ' + mailing_address.province + ' ' + mailing_address.postal_code)          
