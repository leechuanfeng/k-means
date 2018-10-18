
import numpy as np
import math
import operator
from scipy.spatial import distance
import time
import scipy.special
from numpy import linalg
import matplotlib.pyplot as plt

def run():
	X = dataNorm(loadData("2010825.txt"))

	Kval = 50
	M = np.copy(X[0:Kval, 0:X.shape[1]-1])
	np.savetxt('iniMeans(K=' + repr(Kval) + ')' + '.txt', M, fmt="%.0f")

	newM = M
	newX = X
	numIter = 55 
	f = open('errCompute(K='+repr(Kval)+',numIter='+repr(numIter)+')'+'.txt','w')
	for i in range(numIter):
		newX = Group(newX, newM)
		newM = calcMeans(newX, newM)
		err = errCompute(newX, newM)
		f.write(repr(err))
		f.write('\n')
	f.close()
	
	#PLOT THE CLUSTER  
	colors = np.array([	'#377eb8', '#ff7f00', '#4daf4a',
						'#f781bf', '#a65628', '#984ea3',
						'#999999', '#e41a1c', '#dede00'])
	for k in range(len(newX)):
		plt.scatter(newX[k, 0], newX[k, 1], marker='.', c= colors[int((newX[k, 2])%9)])	
	plt.scatter(newM[:, 0], newM[:, 1], marker='*',c='black', s=100)
	plt.show()
	

def errCompute(X, M):
	#this will not have the output from the original array
	N = len(X)								#number of dataset
	atSz = len(X[0])						#number of attribute
	tempX = X[:, 0:atSz-1]					#x,y 

	Msize = len(M)
	sum = 0

	for k in range(len(tempX)):
		tmp = int(X[k][2])
		sum += linalg.norm(tempX[k] - M[tmp])

	#sum all values & find error value
	err = sum/N
	
	return float(err)

def Group(X, M):
	newX = X;
	N = len(X)								#number of dataset
	atSz = len(X[0])						#number of attribute
	tempX = X[:, 0:atSz-1]					#x,y 
	Msize = len(M)
	C=np.zeros(X.shape[0])

	# Cluster assignment step
	for k in range(len(tempX)):
		min = linalg.norm(tempX[k] - M[0]) 	# get first distance
		for i in range(Msize):
			dist = linalg.norm(tempX[k] - M[i])

			if (dist < min):
				C[k] = i 					#assign the centroid to it
				newX[k][2] = i				
				min = dist

	return newX

def calcMeans(X, M):
	atSz = len(X[0])						#number of attribute
	C = X[:, atSz-1:atSz]					#x,y 
	Msize = len(M)
	CNumPt=np.zeros(Msize)
	CX=np.zeros(Msize)
	CY=np.zeros(Msize)
	
	#Move Centroid step
	for j in range(len(C)):
		tmp = int(C[j])

		CNumPt[tmp] += 1
		CX[tmp] += X[j][0]
		CY[tmp] += X[j][1]
	
	newM = []
	for m in range(len(M)):
		if (CNumPt[m] > 0):
			newM.append([CX[m]/CNumPt[m],CY[m]/CNumPt[m]])
	newM =np.asarray(newM)

	return newM
		
def loadData(Filename):
	X=[]
	count = 0
	
	text_file = open(Filename, "r")
	lines = text_file.readlines()
	
	for line in lines:
		X.append([])
		words = line.split('\t')
		for word in words:
			X[count].append(float(word))
		count += 1
	return np.asarray(X)
	
def testNorm(X_norm):
	xMerged = np.copy(X_norm[0])
	#merge datasets
	for i in range(len(X_norm)-1):
		xMerged = np.concatenate((xMerged,X_norm[i+1]))
	print np.mean(xMerged,axis=0)
	print np.sum(xMerged,axis=0)
	
def dataNorm(X):
	X_Norm = X
	n,m = X_Norm.shape 						# for generality
	X0 = np.zeros((n,1))
	X_Norm = np.hstack((X_Norm,X0))
	return X_Norm
	
