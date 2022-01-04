'''
Instruction. 
- Most questions aim to check your knowledge gained from the lecture video. Please try this assignment after watching the video
- The total point is 100pts  (for standard questions) plus 25pts (for challenge questions). When calculating the course grade, we will scale the total point (125pts) to 4%. 
- Grading Rubric
	All the questions of Week2 are programming questions. Your programs will be graded with test cases that we keep in secret. If your program pass every test case, you will get full marks. Otherwise partial credits will be given based on how many secret test cases your programs passed. 

This file contains all the questions for the Assignment 2. 
After completing all the questions, upload the file before the deadline (September 16th, 2021. 11:59pm). Any submission after 72 hours (3 days) from the deadline will get zero credit. 
'''

''' 
QUESTION 1. What is the lowest version of Python that you can use in this course? 
'''
# UN-COMMENT THE NEXT LINE AND TYPE THE ANSWER  
# lowestVersionOfPython = __YOUR ANSWER HERE__


'''
QUESTION 2. The method "fullName" accepts two parameters (firstName and lastName). Complete the method to return the full name in the format of {lastName}, {firstName}
	[Hint]. https://www.w3schools.com/python/gloss_python_string_concatenation.asp
	[Note]. You should not print. Just return a text value. (The same note applies to the other questions)
	E.g. fullName("Tak Yeon","Lee") should return "Lee, Tak Yeon"
'''
def fullName(firstName, lastName):
	return # REMOVE THIS LINE AND COMPLETE THIS METHOD


'''
QUESTION 3. The method "removeWhiteSpace" accepts one string parameter. The string parameter accepts values that contain whitespaces on the left and the right side of the middle content. Complete the method to return a string without such whitespaces.  
	[Hint]. https://www.w3schools.com/python/ref_string_strip.asp
	E.g. removeWhiteSpace("   python ") should return "python"
'''
def removeWhiteSpace(stringWithWhitespace):
	return # REMOVE THIS LINE AND COMPLETE THIS METHOD 


'''
QUESTION 4. The method "calculateVolume" accepts three Numbers (e.g. width, height, depth). Complete the method to return the volumn of the box.
	E.g. calculateVolume(2,3,4) should return 24
'''
def calculateVolume(width, height, depth):
	return # REMOVE THIS LINE AND COMPLETE THIS METHOD 


'''
QUESTION 5. The method "addTwoNumbersInText" accepts txt, a text parameter containing two numbers (e.g. "Add 1 and 2"). Complete the method to return the sum of the two numbers(e.g. 3).  
	[Hint]. Split the input; Access i-th (e.g. 4th) element in the list; Convert text to int 
	E.g. addTwoNumbersInText("Add 3 and 5") should return 8 
'''
def addTwoNumbersInText(txt):
	return # REMOVE THIS LINE AND COMPLETE THIS METHOD 


'''
QUESTION 6. The method "getTheSecondLastElement" accepts a list parameter. Complete the method to return the second last element.  
	[Hint]. Use negative position index (https://knowledgehills.com/python/negative-indexing-slicing-stepping-comparing-lists.htm) 
	E.g. getTheSecondLastElement([1,2,3,4,5]) should return 4
	E.g. getTheSecondLastElement([1,2,3,4,5,6]) should return 5
	E.g. getTheSecondLastElement([1]) <- Don't worry about lists containing less than two elements
	E.g. getTheSecondLastElement([]) <- Don't worry about lists containing less than two elements
'''
def getTheSecondLastElement(lst):
	return # REMOVE THIS LINE AND COMPLETE THIS METHOD 


'''
QUESTION 7. The method "getTheFirstThreeElements" accepts a list parameter. Complete the method to return the first three elements.  
	E.g. getTheFirstThreeElements([1,2,3,4,5]) should return [1,2,3]
	E.g. getTheFirstThreeElements([1,2]) should return [1,2]
	E.g. getTheFirstThreeElements([1]) should return [1]
	E.g. getTheFirstThreeElements([]) should return []
'''
def getTheFirstThreeElements(lst):
	return # REMOVE THIS LINE AND COMPLETE THIS METHOD 


'''
QUESTION 8. The method "updateNthElement" accepts three parameters - a list to update, an index number of the element to update, and a new value. Complete the method to return the updated list.  
	[Note]. If the index number is greater than the list's length, return the original list instead of throwing an error message.  
	E.g. updateNthElement([1,2,3,4,5], 2, "a") should return [1,2,"a",4,5]
	E.g. updateNthElement([1,2,3,4,5], 10, "a") should return [1,2,3,4,5]
'''
def updateNthElement(lst, idx, value):
	return # REMOVE THIS LINE AND COMPLETE THIS METHOD 


'''
QUESTION 9. The method "sortList" accepts a list parameter containing text values. Complete the method to return the list sorted in alphabetical order.  
	[Note]. Assume the input list only contains text values  
	E.g. sortList(["b","a","c"]) should return ["a","b","c"]
'''
def sortList(lst):
	return # REMOVE THIS LINE AND COMPLETE THIS METHOD 



'''
QUESTION 10. The method "countElements" accepts a list parameter. Complete the method to return the number of elements in the list.  
	[Hint]. The answer is quite simple 
	E.g. countElements([0,0,0,0]) should return 4 
'''
def countElements(lst):
	return # REMOVE THIS LINE AND COMPLETE THIS METHOD 



'''
QUESTION 11. The method "mirrorList" accepts a list parameter. Complete the method to return a mirrored version of it.  
	[Hint] Use reverse(lst); Merge two lists (L1,L2) by L1+L2 
	E.g. mirrorList([1,2,3]) should return [1,2,3,3,2,1]
'''
def mirrorList(lst):
	return # REMOVE THIS LINE AND COMPLETE THIS METHOD 




'''
QUESTION 12. The method "welcomePeople" accepts a list parameter containing names. Complete the method to return welcome messages to each of them.  
	[Hint] Use for-loop (e.g. for ... in ...)
	E.g. welcomePeople(["tak","rob","bob"]) should return 
			"Welcome tak! Welcome rob! Welcome bob!" 
'''
def welcomePeople(names):
	return # REMOVE THIS LINE AND COMPLETE THIS METHOD 



'''
QUESTION 13. The method "countN" accepts one number parameter. Complete the method to return a text that count from 1 to N
	[Hint]. Use range(n) to generate a list containing 0 to n-1
	[Note]. You should not print. Just return a text value
	E.g. countN(5) should return "1 2 3 4 5"
'''
def countN(n):
	return # REMOVE THIS LINE AND COMPLETE THIS METHOD 



'''
QUESTION 14. The method "findPersonOlderThan" accepts one nested-list parameter containing a list of name and age pairs (e.g. (["Tak", 15], ["Rob", 20], ["Bob", 28]]).  Complete the method to return names who's age is equal or greater than 18. 
	E.g. findPersonOlderThan([["Tak",15],["Rob",20],["Bob", 28]]) should return ["Rob","Bob"] because Tak's age is below 18
'''
def findPersonOlderThan(nameAndAge):
	return # REMOVE THIS LINE AND COMPLETE THIS METHOD 


'''
QUESTION 15. The method "findPersonWithin" accepts one nested-list parameter containing a list of name and age pairs (e.g. (["Tak", 15], ["Rob", 20], ["Bob", 28]]).  Complete the method to return names who's age is equal or greater than 20, and smaller than 30. 
	[Hint]. You can use either (1) "if ... and ...", or (2) "if ... elif ... else"
	E.g. findPersonWithin([["Tak",20],["Rob",29],["Bob", 40]]) should return ["Tak","Rob"] because both are >=20 and <30. 
'''
def findPersonWithin(nameAndAge):
	return # REMOVE THIS LINE AND COMPLETE THIS METHOD 



'''
QUESTION 16. The method "membershipTest" accepts two parameters (a list, and a value). Complete the method to return True (the list contains the value) or False (the list does not contain the value).  
	[Hint]. Use "if ... in ..." command
	E.g. membershipTest([3,1,5,2], 2) should return True
	E.g. membershipTest([3,1,5,2], 4) should return False 
	E.g. membershipTest(["a","b","d"], "a") should return True 
	E.g. membershipTest(["a","b","d"], "c") should return False 
'''
def membershipTest(lst, val):
	return # REMOVE THIS LINE AND COMPLETE THIS METHOD 



'''
QUESTION 17. The method "getColor" accepts a dictionary (e.g. flower names and their colors) and a text parameters (e.g. flower's name that you wonder what color it has). Complete the method to return the color of the requested flower. If the dictionary does not have the requested flower name, it should return "There is no requested flower name] in my knowledge"
	[Hint]. To get a list of keys from a dictionary D, use "D.keys()"
	[Hint]. To check whether a value is in a list, use "if ... in ..."
	E.g. getColor({"daisy":"white", "sunflower":"yellow"}, "sunflower") should return "yellow"
	E.g. getColor({"daisy":"white", "sunflower":"yellow"}, "hahahoho") should return "There is no hahahoho in my knowledge"
'''
def getColor(flowerDict, flowerName):
	return # REMOVE THIS LINE AND COMPLETE THIS METHOD 




'''
QUESTION 18. The method "countFreq" accepts two parameters. The first parameter is a dictionary of text-number pairs that represents event types and their frequencies (e.g. {"visit":2, "purchase":1}). The second parameter is a text value that represents an observed event. Complete the method to count up the given event in the dictionary.  
	E.g. Let's say,
		eventCount = {"visit":1, "purchase":2}
		countFreq(eventCount, "purchase") 
	will update eventCount to be {"visit":1, "purchase":3}
	[Note] You don't need to return anything. Just update the provided dictionary.
'''
def countFreq(D, ev):
	return # REMOVE THIS LINE AND COMPLETE THIS METHOD 


#####################################################################################
#####################################################################################

'''
CHALLENGE 1. The method "getFirstNameInitial" accepts one parameter (fullName) in the format of {lastName}, {firstName}. Complete the method to return the capitalized initials of the first name.
[Hint.] https://www.w3schools.com/python/ref_string_split.asp 
	E.g. getFirstNameInitial("Lee, Tak Yeon") should return "T.Y"
	E.g. getFirstNameInitial("Lee, TakYeon") should return "T"
	E.g. getFirstNameInitial("Lee, TakYeon Zero") should return "T.Z"
	E.g. getFirstNameInitial("Lee, Tak") should return "T"
	E.g. getFirstNameInitial("Lee, tak") should also return "T"
'''
def getFirstNameInitial(fullName):
	return # REMOVE THIS LINE AND COMPLETE THIS METHOD



'''
CHALLENGE 2. The method "addItemTo" accepts three parameters. The first parameter is a dictionary "recipes" that represents pairs of a recipe name and a list of ingredients. For instance, recipes dictionary could be like {"salad":["tomatoes","basil","olive oil"], "pasta":["olive oil","spagetti"]}. The second and the third parameters are text values that represent a recipe name and an ingredient. Complete the method to add the ingredient to the given recipe.  
	[Hint] If the dictionary does not have the recipe yet, you must initialize the recipe as an empty list first. 
	[Note] You don't need to return anything. Just update the provided recipe dictionary.
	[Note] You don't need to consider a situation where the new ingredient is already in the recipe. In other words, a recipe may have same ingredients multiple times. 
	E.g.1 Let's say, 
			D = {"salad":["tomatoes","basil","olive oil"], "pasta":["olive oil","spagetti"]}
			K = "pasta"
			V = "tomato sauce"
		addItemTo(D,K,V) should update D as below
			D = {"salad":["tomatoes","basil","olive oil"], "pasta":["olive oil","spagetti","tomato sauce"]}
	E.g.2 Let's say,
			D = {"salad":["tomatoes","basil","olive oil"]}
			K = "cold noodle"
			V = "ice"
		addItemTo(D,K,V) should update D as below
			D = {"salad":["tomatoes","basil","olive oil"], "cold noodle":["ice"]}	
'''
def addItemTo(recipeDict, recipeName, ingredient):
	return # REMOVE THIS LINE AND COMPLETE THIS METHOD 















