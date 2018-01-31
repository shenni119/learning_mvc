
import csv

data_is_loaded = False

def load_data():

	with open('US_County_Level_Presidential_Results_12-16.csv', 'r') as csvfile:
	    reader = csv.reader(csvfile, delimiter=',')
	    fulltuplist=[]
	    for row in reader:
		    if row[9]=='AK':
			    pass
		    else:
			    fulltuplist.append((row[9],row[2],row[3],row[4]))
			    # fulltuplist.append((type(row[9]),type(row[2]),type(row[3]),type(row[4])))

		    # break
	    return fulltuplist
	    data_is_loaded = True

# print (load_data())

def get_data(party='dem', raw=True, sort_ascending=True, year=2016):
	if not data_is_loaded:
		fulltuplist2=load_data()
	filterinputdict={}
	statetotaldict={}
	# returnlist=[]
	for county in fulltuplist2:
		# returnlist=county[3]
		# returnlist.append(county)
		if county[0]=='state_abbr':
			pass
		else:
			totalvotes=float(county[3])
			demtotal=float(county[1])
			goptotal=float(county[2])
			stateabrev=county[0]
			value=demtotal
			if stateabrev in statetotaldict:
				statetotaldict[stateabrev]+=totalvotes
			else:
				statetotaldict[stateabrev]=totalvotes
			if party=='gop':
				value=goptotal
			if stateabrev in filterinputdict:
				filterinputdict[stateabrev]+=value
			else:
				filterinputdict[stateabrev]=value
	if raw==False:
		for state in filterinputdict:
			filterinputdict[state]=filterinputdict[state]/statetotaldict[state]
	tuplist=list(filterinputdict.items())
			# returnlist.append((stateabrev,demtotal,goptotal,totalvotes))
	if sort_ascending==True:
		tuplist=sorted(tuplist,key=lambda x:x[1])
	else:
		tuplist=sorted(tuplist,key=lambda x:x[1], reverse=True)

	# 	# break
	return tuplist

# print (get_data(party='gop',raw=False))
# # print (get_data())
# test=get_data()
# print (test[0])
# print (test[-1])
# print (type(test))
# print (test)
# print (type(get_data(raw=False)))

	# build the appropriate list of tuples to return

	# return [('A', 1), ('B', 2)]
