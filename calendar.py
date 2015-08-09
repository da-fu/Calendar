#_-------------------Q1----Part a-------------------------------------------------------------------------------------------------#
def get_individual_courses(course_desc_page):
    # This function reads the file of the peage of the website. And transfer each course into the list.
    # Arguement: course_desc_page is the name of the file as a string
    
    page = open(course_desc_page).read()                     # Read the file and store it into the string
    desc = []                                                # set up an empty list
    page_str = page[:]                                       # ransfer the string into list
    for i in range(page.count('<A NAME="')+1):               # for loop: i from 0 to the amount of <A NAME=" in the list
        if page_str.find('<A NAME="') != -1:                 # if there is no more <A NAME="
            desc_str = page_str[page_str.find('<A NAME="'):page_str.find('DR=')] # last one should between the <A NAME=" and DR=
            page_str = page_str[page_str.find('DR=')+14:]    #the reaming string should be the point to the end
            desc.append(desc_str)                            # then the list will add the remaining string
    return desc

#--------------------Q1------part b-----------------------------------------------------------------------------------------------#
def get_course_details(course_description):
    # This function will takes a course description (a str like those in the list returned by get_individual_courses)
    # and returns a list whose first element is the course code as a string
    # Arguement: the course_descritipn is the string witch will store the descriptionof the course
    detail=[]                                                 # set up an empty list to put the detail information
    course_code=''                                            # first make the course_code be empty
    course_code=course_description[course_description.find('<A NAME="')+9:course_description.find('"></A>')]
                                                              # Then the course_code should be between the '<A NAME and the "></A>'
    detail.append(course_code)                                # the tail add the course_code ass the first element
    if course_description.find('Prerequisite:')==-1:          # if there is no prerequistite in the description,
        detail.append([])                                     # the detail information will add the remaining
    else:                                                     # else if there are prerequistists
        prer =course_description[course_description.find('Prerequisite:'):] # find the prerequist and store in the string
        accurate_prer = prer[:prer.find('<BR>')]              # get more accurate prerequisist
        detail.append(accurate_prer)                           # the detiil information 
    return detail

#---------------------Q1------part c-----------------------------------------------------------------------------------------------#
def prereq_str_to_list(prereq_str):
    # This This function takes a string that contains the listings of the prerequisites for a course (like the one returned
    #by get_course_details) and returns a list of course codes and punctuation, in the same order that they appear in prereq_string
    # Arguement: the prereq_str is the strign that contains the prereq info
    prereq_list=[]                                             #set up an empty list
    prereq_str2 = prereq_str[:]                                #and another identity list with arguement
    for i in range(prereq_str2.count('<A HREF="')):             # for loop: for i from 0 to the number of the '<A HREF="'
        index=prereq_str.find('<A HREF="')+21                   # the first index starts at 21 positions after the '<A HREF="'
        prereq_list.append(prereq_str[index:prereq_str.find('">')])  #the prerequisit add the name of the required course
        prereq_list.append(prereq_str[prereq_str.find('</A>')+len('</A>')]) #also append the mark behind the course name
       
        prereq_str = prereq_str[prereq_str.find('</A>')+len('</A>')+1:] # the meaining string should be after the mark
        if prereq_str[1] in ['0','1','2','3','4','5','6','7','8','9']:  # if the first position in the remaining string is a number
            prereq_list.append(prereq_list[-2][:-5]+prereq_str[:5])  #add the title of the previous course to the number
            prereq_list.append(prereq_str[5])                    #also add the mark after the course to the list
            prereq_str = prereq_str[6:]                          # the remaining string will be after the mark
    for letter in prereq_str:                                    #for loop: for every letter in the  prerequirist 
        if letter in ["/",",",".",";"]:                          # if the letter is a mak,
            prereq_list.append(letter)                           # add the mark to the prerequirsit
    answer=[]                                                    # set up an empty list as final answer
    for lis in prereq_list:                                      # for loop: for every element in the prerequirsit 
        if lis != ' ':                                           # if the element is not empty
            answer.append(lis)                                   # add the  element to the final answer
    return [answer]                                               # return the final answer

#---------------------Q1------part d-----------------------------------------------------------------------------------------------#
def expand_one_or(course_lists):
    # This function take the list of the course requirsit, and expand the list when there is "/" lesft in the list
    # Return the list that disovle the list due to the first '/'
    # Arguement: the list of the course requirst with '/' inside
	for j in range(len(course_lists)):                      # for loop: for i from 0 to the length of the list
	    for i in range(len(course_lists[j])):               # for loop: for 
                if i == len(course_lists[j]) and chourse_lists[j][i] in ["/",",",".",";"]:  #if the index equals length of the element and it is a mark
                    course_lists[j] = course_lists[j][:len(course_lists[j])-1] #thr element will delete the last position
                    break                                        # break the loop
                if course_lists[j][i] in ["/",",",".",";"] and course_lists[j][i-1] in ["/",",",".",";"]:
		    # if the element is a mark and the element infront of it is also a mark
                    course_lists[j]= course_lists[j][:i-1]       # the element will delete the remaining string 
                    break                                        # and finish the loop
	
	lis2=[]                                                  #set uo the empty list
	for lis in course_lists:                                 # for every element in the list
	    if '/' not in lis:                                   # if the '/' is not in the list
                lis2.append(lis)                                 # the element will be added
	    if '/' in lis:                                       # if the '/' is in the element
                i=lis.index('/')                                 # find the index
                if lis[i] == '/' and lis[i-1] not in ["/",",",".",";"] and lis[i+1] not in ["/",",",".",";"]:
		    # if the elemet is a mark and the closet is not mark
                    half1=lis[:i-1]+lis[i+1:] #separate the list
                    half2=lis[:i]+lis[i+2:]
                    lis2.append(half1)        # add the front half
                    lis2.append(half2)        # add the back half
	course_lists=lis2[:]                  # the final answer is same to the list
	return course_lists                   # return the final answer
    
    
#---------------------Q1------part e----------------------------------------------------------------------------------------------#
def expand_all_ors(course_lists):
    # this function takes the list of the prerequisit list and return the list expanded without '/' inside
    #Arguement: the course requirist list
    for j in range(len(course_lists)):                                #for loop: for j in the list
        for i in range(len(course_lists[j])):                         #for i in the element in the list
            if i == len(course_lists[j])-1 and course_lists[j][i] in ["/",",",".",";"]: # if the i index match and not a mark
                course_lists[j] = course_lists[j][:len(course_lists[j])-1] # j is changed
                break                                                  #finish the loop
            if i==0 and course_lists[j][i] in ["/",",",".",";"]:      # if the element is in the mark list
                course_lists[j] = []                                   # make it be empty list
                break                                                  # finish the loop
            if course_lists[j][i] in ["/",",",".",";"] and course_lists[j][i-1] in ["/",",",".",";"] :   # if the element is in the list
                course_lists[j] = course_lists[j][:i-1]               # the list is changed
                break                                                  # finish the loop
    ans = {}                                                           # set uo the empty dictionary
    result = []                                                        # set up the empty list
    ans[0] = course_lists[:]                                           # let the list store in the dictionary
    current_most=0                                                     # count the current most '/' as 0
    for i in course_lists:                                             # for every one in the list
        if i.count('/')> current_most:                                 # if the couted number is more than the current most
            current_most = i.count('/')                                # change it to the current most
    for i in range(1,current_most+1):                                  # for every one in the most
        ans[i] = expand_one_or(ans[i-1])                               # answer equals to the first expanded one
    result = []                                                        # set uo the empty list
    for j in ans[current_most]:                                         # for everyone in the last dictionary
        if j not in result:                                            # if the one is not inside
            result.append(j)                                           #result add it
    for i in range(len(result)):                                       # for the i in length of the dictionary
        result[i] = sorted(result[i])[:]                               # sort it
	
    answer=[]                                                           # set up final answer
    for i in range(len(result)):                                        # for everyone in the result
        answer.append([])                                               # answer add one empty list
        for j in range(len(result[i])):                                 # for the one in the list
            if result[i][j] not in answer[i] and result[i][j] not in ["/",",",".",";"]:  # if is not repeating
                answer[i].append(result[i][j])                          # add it to the answer
    answer = sorted(answer)                                             # sort the answer
    return answer                                                       # return it


#------------------------------------Q1------------------------------------------------------------------------------------------#
def build_prerequisite_dict(course_desc_page):
    # This function takes the string of the file name and return the expanded dictionary
    # Arguement: the string of the file name
    course_dict = {}                                     #set uo the final dictionary
    desc = get_individual_courses(course_desc_page)      # get the course prerequirsit
    for i in range(len(desc)):                           # for everyonr in the course
        a=get_course_details(desc[i])                    # get the details form the function
        b=prereq_str_to_list(a[1])	                # get the prerequirsit 
        course_dict[a[0]] = expand_all_ors(b)            # add it to the dictionary
    return course_dict                                   # return the final answer



# ---------------------------------------------Q2--------------------------------------------------------------------------------#
def check(list_x,init_prereq_dict):
   # this functin is used to check is the elements in the list are simpilfied
   # Arguement: the list and the prerequistist dictionary
    done = 0                                        # let the done sign be 0
    for i in list_x:                                # for everyonr in the list
        for j in i:                                 # for every one in the element
            b_done = 0                              # let the second done sign be 0
            if j not in init_prereq_dict:           # if the element is not in the dictionary
                done=0                              # it means done 
            elif init_prereq_dict[j] == [[]]:         # if the course is most simple in the dictionary
                done=0                              # it also means done
            elif init_prereq_dict[j] != [[]] and j in init_prereq_dict: # if the course is not simplified
                for k in i:                         # for everyone in the element
                    if [k] in init_prereq_dict[j] or k not in init_prereq_dict : 
			                    # if the course is in the next level
                        b_done = 1         # it means the list is done
                if b_done == 1:            # if second sign is 1
                    done = 0               # first sign should be done
                elif b_done == 0:          # other wise
                    done = 1               # the done sign should be 1
                    break                  # finish the loop
        if done == 1:                      # if the list is done
            break                          # finish the loop
    if done == 0:                          # if the list is done 
        return True                        # return it is true
    elif done == 1:                        # else if the list is not done
        return False                       # return false

		
def findout(list_x,init_prereq_dict):      
    # this function takes the list and check with element is not most simple
    #arguement: the list od course and the dictionary of the course requirsit
    done = 0                                                         # let the done sign be 0                         
    d = ''                                                           #answer be an empty string
    for i in list_x:                                                 # for everyonr in the list
        for j in i:                                                  # for every one in the element
            b_done = 0                                               # let the second done sign be 0
            if j not in init_prereq_dict:                            # if the element is not in the dictionary
                done=0                                               # it means done 
            elif init_prereq_dict[j]==[[]]:                            # if the course is most simple in the dictionary
                done=0                                                # it also means done
            elif init_prereq_dict[j] != [[]] and j in init_prereq_dict:# if the course is not simplified
                for k in i:                                          # for everyone in the element
                    if [k] in init_prereq_dict[j] or k not in init_prereq_dict:                   # if the course is in the next level
                        b_done =1                                      # it means the list is done
                if b_done == 1:                                      # if second sign is 1
                    done = 0                                         # first sign should be done
                elif b_done == 0:                                    # other wise
                    done = 1                                         # the done sign should be 1
                    d = j                                            #the answer is the element
                    break                                             # finish the loop
        if done ==1:                                                 # if the list is done 
            break                                                    # finish the loop
    if done == 0:                                                    # if the list is done 
        return True                                                  # return it is true
    elif done == 1:                                                  # else if the list is not done
        return d                                                     # return the final answer
	    
def add_to_next_level(list_x,init_prereq_dict):
    # this function add the next level list to the list
    # Arguements: the list and the course dictionary
    answer=[]   # set up the empty list
    for i in list_x:                                 # for everyone in the ;ist
        if check([i],init_prereq_dict) == True:        # if the check is true
            answer.append(i)                          # add it
        if check([i],init_prereq_dict) == False:     #if the check is false
            x=findout([i],init_prereq_dict)             # findout which one is not simpliied
            for j in range(len(init_prereq_dict[x])): # for everyone in the courselist dictionary
                a=init_prereq_dict[x][j]              #add it to the answer
                answer.append(i+a)                  # add to the answer
    return answer                                   # return the final answer

def sort_and_simplify(list_x,init_prereq_dict):
    # this function takes the string and sort it and delete some repeating elements
    # Return the string that is sorted
    # Arguement: the list and the course dictionary
    answer=[]                                  #set up a empty list
    result =[]                                 # set up another empty list
    for i in range(len(list_x)):               # for loop : for all elements in the list
        answer.append([])                      # the answer add an empty list
        for j in range(len(list_x[i])):         #for all elements in the element
            if list_x[i][j] not in answer[i]:  #if the elements is not in the list
                answer[i].append(list_x[i][j]) # add it
    answer = sorted(answer)                    # let the final be the answer
    for i in answer:                           # for everyone in the list
        result.append(sorted(i))               # sort them
    return result                              # return the final result


def get_all_paths_to_course(course_code, init_prereq_dict):
   #This function takes a course code course_code (as a str) and a dictionary init_prereq_dict (which has
   #the same format as the dictionary returned by build_prerequisite_dict), and returns the list of lists of
   #all the possible ways to satisfy the prerequisites for course course_code.
   #Arguement: the sourse_code as a string, and the dictionary of the course prerequistist 
    answer=[]                                                # set up an empty list as the final answer
    result = init_prereq_dict[course_code]                   # the result means the initial list form the course dictionary
    while check(result, init_prereq_dict) == False:          # while loop: while the list is not tcompleted simiplfied 
        result = add_to_next_level(result,init_prereq_dict)  # result means the output of the return after add_to_next_level function 
        result = sort_and_simplify(result,init_prereq_dict)  # go throgh the function to be correct formated
    for i in result:                                         # for loop: foe every one in the list
        answer.append(sorted(i))                             # answer add the sorted list
    return answer                                            # return the final answer






#-----------------------------test-----------------------------------------------------------------------------------------------#

if __name__ == '__main__':
       
    #Test 1: when a course has only one prerequired course:
    print('Test 1')
    course_code = 'A'
    init_prereq_dict = {'A':[['B']]}
    print(get_all_paths_to_course(course_code, init_prereq_dict)) 
    #should return [['B']]
    
    #Test 2: when a course has no prerequired course:
    print('Test 2')
    course_code = 'A'
    init_prereq_dict = {'A':[[]]}
    print(get_all_paths_to_course(course_code, init_prereq_dict)) 
    #should return [[]]
    
    #Test 3: when a course has multiple prerequired courses:
    print('Test 3')
    course_code = 'A'
    init_prereq_dict = {'A':[['B'],['C'],['D'],['E']]}
    print(get_all_paths_to_course(course_code, init_prereq_dict)) 
    #should return [['B'], ['C'], ['D'], ['E']]   
    
    #Test 4: when a course has multiple options on prerequired courses:
    print('Test 4')
    course_code = 'A'
    init_prereq_dict = {'A':[['B','C','D'],['E','F']]}
    print(get_all_paths_to_course(course_code, init_prereq_dict)) 
    #should return [['B', 'C', 'D'], ['E', 'F']]    
    
    #Test 5: when one course has multiple prerequired courses and one of the prerequired course has one prerequired course:
    print('Test 5')
    course_code = 'A'
    init_prereq_dict = {'A':[['B'],['C'],['D'],['E']],'C':[['K']]} 
    print(get_all_paths_to_course(course_code, init_prereq_dict)) 
    #should return [['B'], ['C', 'K'], ['D'], ['E']]
    
    #Test 6: when one course has multiple prerequired courses and one of the prerequired course has multiple prerequired courses:
    print('Test 6')
    course_code = 'A'
    init_prereq_dict = {'A':[['B'],['C'],['D'],['E']],'C':[['K'],['G']]} 
    print(get_all_paths_to_course(course_code, init_prereq_dict)) 
    #should return [['B'], ['C', 'G'], ['C', 'K'], ['D'], ['E']]
    
    #Test 7: when one course has multiple prerequired courses and double chains:
    print('Test 7')
    course_code = 'A'
    init_prereq_dict =  { "A": [ ["B"], ["C"] ],"B": [ ["D"], ["E"] ],"D": [ ["F"], ["G"] ]}    
    print(get_all_paths_to_course(course_code, init_prereq_dict)) 
    #should return [['B', 'D', 'F'], ['B', 'D', 'G'], ['B', 'E'], ['C']]    
    
    #Test 8: when one course has multiple prerequired courses and multiple chains: 
    print('Test 8')
    course_code = 'A'
    init_prereq_dict =  { "A": [ ["B"], ["C"] ],"B": [ ["D"], ["E"] ],"D": [ ["F"], ["G"] ],"G": [ ["Z"], ['Q']]}    
    print(get_all_paths_to_course(course_code, init_prereq_dict)) 
    #should return [['B', 'D', 'F'], ['B', 'D', 'G', 'Q'], ['B', 'D', 'G', 'Z'], ['B', 'E'], ['C']]
    
 
   
