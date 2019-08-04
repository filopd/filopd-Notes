#List of 3 countries
lstCountry = ["India", "China", "Nepal"]
print("List of Countries:", lstCountry)
#Add Country at the end
lstCountry.append("Pakistan")
print("List of Countries:", lstCountry)
#Remove Country By Index
lstCountry.pop(2)
print("List of Countries:", lstCountry)
#Add Country in the Middle
mid= int(len(lstCountry)/2)
lstCountry.insert(mid, "Shri Lanka")
print("List of Countries:", lstCountry)
print("---------------------------------")
#Above using Set
#List of 3 countries
lstCountry = {"India", "China", "Nepal"}
print("List of Countries:", lstCountry)
#Add Country at the end
lstCountry.add("Pakistan")
print("List of Countries:", lstCountry)
#Remove Country By Index
lstCountry.remove("China")
print("List of Countries:", lstCountry)
#Add Country in the Middle (not ordered so random)
lstCountry.add("Shri Lanka")
print("List of Countries:", lstCountry)

