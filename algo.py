def combinaison(L): 
    
    for i in range(10): 
        for j in range(i+1,10): 
            for k in range(j+1,10): 
                
                if (i!=(j and k) and j!=(i and k) and k!=(j and i)):  
                    print(L[i],L[j],L[k]) 
                    
combinaison([0,1,2,3,4,5,6,7,8,9])