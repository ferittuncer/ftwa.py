#!/usr/bin/python3

import ftwa
import unittest
import os
import re
import time
from datetime import date

Veli 	= ftwa.Person("Veli", "Yanyatan",   "male", date(2005, 12, 15), date(2075, 12, 15))	#Çocuk	
Ali 	= ftwa.Person("Ali", "Yanyatan",    "male", date(1980, 12, 15), date(2055, 12, 15)) # Baba
Huri 	= ftwa.Person("Huri", "Yanyatan", "female", date(1983, 12, 15), date(2075, 12, 15)) # Anne
Deli 	= ftwa.Person("Deli", "Yanyatan",   "male", date(2007, 12, 15), date(2075, 12, 15)) # Çocuk

G = ftwa.FamilyGraph()

G.person_list.append(Veli)
G.person_list.append(Huri)
G.person_list.append(Deli)
G.person_list.append(Ali)

G.new_relation(Veli, ftwa.Relation.SPOUSE, Huri)
G.new_relation(Veli, ftwa.Relation.CHILD, Ali)
G.new_relation(Veli, ftwa.Relation.CHILD, Deli)
G.new_relation(Huri, ftwa.Relation.CHILD, Ali)
G.new_relation(Huri, ftwa.Relation.CHILD, Deli)


class Test(unittest.TestCase):

	def test_overall(self):


	
		assert Veli.is_placeholder() == False
		assert Deli.is_placeholder() == False
		assert Ali.is_placeholder() == False
		assert Huri.is_placeholder() == False

	def test_get_age(self):
		date1 = date(2016, 12, 14)
		date2 = date(2016, 12, 15)
		date3 = date(2016, 12, 16)

		birthdate = Ali.birthdate
		assert 35 == (date1.year - birthdate.year - ((date1.month, date1.day) < (birthdate.month, birthdate.day)))
		assert 36 == (date1.year - birthdate.year - ((date2.month, date2.day) < (birthdate.month, birthdate.day)))
		assert 36 == (date1.year - birthdate.year - ((date3.month, date3.day) < (birthdate.month, birthdate.day)))

	def test_is_alive(self):
		date1 = date(2055, 12, 14)
		date2 = date(2055, 12, 15)
		date3 = date(2055, 12, 16)

		deathdate = Ali.deathdate

		assert True == (0 >(date1.year - deathdate.year - ((date1.month, date1.day) < (deathdate.month, deathdate.day))))
		assert False == (0 >(date1.year - deathdate.year - ((date2.month, date2.day) < (deathdate.month, deathdate.day))))
		assert False == (0 >(date1.year - deathdate.year - ((date3.month, date3.day) < (deathdate.month, deathdate.day))))

	def test_get_level(self):

		assert 0 == G.get_level(Ali)
		assert 0 == G.get_level(Huri)
		assert 1 == G.get_level(Deli)
		assert 1 == G.get_level(Veli)

	def test_get_first_degree_relatives(self):
		print(len(Ali.get_first_degree_relatives()))
		assert 3 == len(Ali.get_first_degree_relatives())
		assert 3 == len(Huri.get_first_degree_relatives())
		assert 3 == len(Veli.get_first_degree_relatives())
		assert 3 == len(Deli.get_first_degree_relatives())
		
	

	def test_str(self):
		Veli.str()
		Deli.str()
		Ali.str()
		Huri.str()
if __name__ == '__main__':
	unittest.main()



