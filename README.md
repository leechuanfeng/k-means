# k-means
Using k-means clustering algorithm to learn the clustering partitioning method from the training data, and getting familiarized on determining the parameter K for k-means algorithm.

To try out this project, run the following lines in cmd in sequence:

Instructions:

```sh
$ python
$ import os
$ os.chdir("C:\Users\username\Desktop\py-kmeans")
$ import kmeans
$ kmeans.run()
```

### Abstract
K-means clustering algorithm is a unsupervised machine learning algorithm, a method of vector quantization where we aim to partition n observations into k clusters in which each observation belongs to the cluster with the nearest mean. We will observe how our clustering algorithm can group the lightning strokes basing on the position. 

### Attribute Information 
- 1. latitude 
- 2. longitude 
 
 
### Lightning data 
![fig1](https://github.com/leechuanfeng/k-means/blob/master/images/fig1.png "fig1")

### Objective Function 
The objective function is also very similar to our regression error function. But this time around we want to find the minimum distance between each medoid. By dividing with N, the number of dataset will give us a mean value. 

![fig1.2](https://github.com/leechuanfeng/k-means/blob/master/images/fig1.2.png "fig1.2")

The objective function is later used in our cluster assignment step by fixing M and in move centroid step by fixing C.  
 
### Assigning Objects 
The way to start assigning object, is to select points as our centroid, to do it effectively, we randomly select k number of data points as our centroid, the reason for doing this is so that we would not end up with centroid too far away from our dataset which might end up with zero data point assigned to it and hence being removed. After which, we will proceed to do our cluster assignment step which is assigning all the datapoint to a cluster centroid nearest to it and continuing to our move centroid step, which we will discuss next.

```sh
PSEUDO CODE:
Step 1: Randomly pick k data points as our centroid 
Step 2:  
Repeat 
{ 
  // cluster assignment step 
  for i = 1, 2, …, N (training samples) 
  { 
    𝑐𝑖 = 𝑚𝑖𝑛𝑘(||x𝑖 − 𝜇𝑘||^2)
    (for i = 1, 2, …, k) 
  } 
  // move centroid step 
  // … 
} 
```

### Updating Means 
After we are done with our cluster assignment step, next we have to do our move centroid step, which is calculating the new mean value with all the points assigned to each centroid. In another words, we take the average of the sum of the points assigned to that centroid, we update the mean value for that cluster, and repeat for every other cluster. Finally, we will repeat the entire algorithm again from step 2 until there is no change to the clustering result.  
 
 ```sh
PSEUDO CODE:
Step 1: Randomly pick k data points as our centroid 
Step 2:  
Repeat 
{ 
  // cluster assignment step  
  // … 
 
  // move centroid step 
  for k = 1, 2, …, K  
  { 
    𝜇𝑘 = 𝑎𝑣𝑔 𝑜𝑓 𝑡ℎ𝑒 𝑝𝑜𝑖𝑛𝑡𝑠 𝑎𝑠𝑠𝑖𝑔𝑛𝑒𝑑 𝑡𝑜 𝑐𝑙𝑢𝑠𝑡𝑒𝑟 𝑘  
  } 
}
 ```
 
### Choosing K 
When K is low, the algorithm runs much faster as compared to when K gets bigger. Depending on how well the initial clusters are assigned, the number of iteration differs to reach the point where there is no change to the clustering result. 

![fig2](https://github.com/leechuanfeng/k-means/blob/master/images/fig2.png "fig2")

From the table above, we can see how each k value reaches the point the point where there is no change to the clustering result from the highlighted values.

### Results
![fig3](https://github.com/leechuanfeng/k-means/blob/master/images/fig3.png "fig3")
![fig4](https://github.com/leechuanfeng/k-means/blob/master/images/fig4.png "fig4")

Depending on how the meteorologists want to group the lightning strokes, let’s say for example by the continent like Europe, Asia and so on, they can use a K value lesser than or equal to 50, or if they would like to go into more detail like the countries, or city, they may consider using a K value more than or equal to 100. 
