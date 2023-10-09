from sklearn import tree


Names = ["Tenis","Tenis","Cricket","Tenis","Cricket","Tenis","Cricket","Tenis","Tenis","Tenis","Cricket","Tenis","Cricket","Tenis","Cricket"]

BalllsFeatures = [[35,"Rough"],[47,"Rough"],[90,"Smooth"],[48,"Rough"],[90,"Smooth"],[35,1],[92,"Smooth"],[35,"Rough"],[35,"Rough"],[35,"Rough"],[96,"Smooth"],[43,"Rough"],[110,"Smooth"],[35,"Rough"],[95,"Smooth"]]

clf = tree.DecisionTreeClassifier()     

clf = clf.fit(BalllsFeatures,Names)     

print(clf.predict([[44,1],[43,1][44,1][97,0]]))                
















