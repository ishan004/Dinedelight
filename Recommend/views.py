from django.shortcuts import render
import pickle
import numpy as np
import pandas as pd

with open('popular.pkl', 'rb') as file:
        popular_data = pd.read_pickle(file)
with open('chitwan.pkl', 'rb') as file1:
        chitwan = pd.read_pickle(file1)
    
with open('pt.pkl', 'rb') as file2:
    pt = pd.read_pickle(file2)
    
with open('similarity_scores.pkl', 'rb') as file3:
    similarity_scores = pd.read_pickle(file3)
# Create your views here.
def popular_view(request):
   
    data = [] 
    for i in popular_data.index:
        data.append({
                'Title': popular_data.loc[i, 'Title'],
                'location':popular_data.loc[i, 'location'],
                'Image_URL': popular_data.loc[i, 'Image_URL'],
                'ratings': popular_data.loc[i, 'avg_ratings']
            })
            
        context={'restros': data}       
            
    
    return render(request, 'recommend/popular.html',context=context)

def recommend_ui(request):
    return render(request, 'recommend/recommendation.html')

def recommend_view(request):

    if request.method == 'POST':
        restaurant_name = request.POST.get('restaurant_name')
        
        if restaurant_name not in pt.index:
            error_message = f"Error: {restaurant_name} not found in the data."
            return render(request, 'recommend/recommendation.html', {'error_message': error_message})
        
        index = np.where(pt.index == restaurant_name)[0][0]
        similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]
    
        data1 = []
        for i in similar_items:
            item = []
            temp_df = chitwan[chitwan['Title'] == pt.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('Title')['Title'].values))
            item.extend(list(temp_df.drop_duplicates('Title')['location'].values))
            item.extend(list(temp_df.drop_duplicates('Title')['Image_URL'].values))
        
            data1.append(item)
        context = {'data1': data1}
        
    return render(request, 'recommend/recommendation.html',context=context)
        

