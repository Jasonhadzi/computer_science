#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:41:29 2021

@author: jasonhadzikostas
"""

class Patient:
  def __init__(self, name, age,sex,bmi,num_of_children,smoker):
    self.name = name
    self.age = age
    self.sex = sex
    self.bmi = bmi
    self.num_of_children = num_of_children
    self.smoker =smoker
  
  def estimated_insurance_cost(self):
    estimated_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500
    print(self.name + 's estimated insurance costs is '+ str(estimated_cost) +' dollars.')
    return estimated_cost
  
  def update_age(self,new_age):
    self.age = new_age
    print(self.name + " is now " + str(self.age) + " years old.")
    self.estimated_insurance_cost()

  def update_num_children(self, new_num_children):
    self.num_of_children = new_num_children
    if self.num_of_children == 1:
      print(self.name + " has " + str(self.num_of_children) + " child.")
    else:
      print(self.name + " has " + str(self.num_of_chilrden) + " children.")
    self.estimated_insurance_cost()
  
  def patient_profile(self):
    patient_information ={}
    patient_information["Name"] = self.name
    patient_information["Age"] = self.age
    patient_information["Sex"] = self.sex
    patient_information["BMI"] = self.bmi
    patient_information["Number of Children"] = self.num_of_children
    patient_information["Smoker"] = self.smoker
    return patient_information


    


patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)
print(patient1.name)
patient1.estimated_insurance_cost()
patient1.update_age(26)
patient1.update_num_children(1)

print(patient1.patient_profile())