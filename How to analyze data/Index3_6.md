# 한국 넷플릭스 프로그램 상영시간 확인하기

## 추가 문제 설명

한국 넷플릭스 TV프로그램, 영화의 상영시간은 어떻게 구성되어 있을까? 시각화해보자

## 학습목표

목적에 맞게 시각화하기

## 답안1 - TV 프로그램

```python
netflix_rok_shows['duration'].unique()
결과) array(['1 Season', '2 Seasons', '5 Seasons', '4 Seasons', '3 Seasons'],
      dtype=object)
```

```python
colors = ['lightslategray']
colors[0] = 'crimson'

show_dur = pd.value_counts(netflix_rok_shows['duration'])
fig = go.Figure([go.Bar(x=show_dur.index, y=show_dur.values,
                        text=show_dur.values, marker_color=colors)])
fig.update_traces(textposition='outside')
fig.update_layout(title='한국 TV 프로그램 상영시간 분포도', xaxis={'categoryorder':'total descending'})

fig.show()
```

![%E1%84%92%E1%85%A1%E1%86%AB%E1%84%80%E1%85%AE%E1%86%A8%20%E1%84%82%E1%85%A6%E1%86%BA%E1%84%91%E1%85%B3%E1%86%AF%E1%84%85%E1%85%B5%E1%86%A8%E1%84%89%E1%85%B3%20%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%84%80%E1%85%B3%E1%84%85%E1%85%A2%E1%86%B7%20%E1%84%89%E1%85%A1%E1%86%BC%E1%84%8B%E1%85%A7%E1%86%BC%E1%84%89%E1%85%B5%E1%84%80%E1%85%A1%E1%86%AB%20%E1%84%92%E1%85%AA%E1%86%A8%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%92%E1%85%A1%E1%84%80%20b1645bc0778e4e42b86e4dc09e030403/Untitled.png](%E1%84%92%E1%85%A1%E1%86%AB%E1%84%80%E1%85%AE%E1%86%A8%20%E1%84%82%E1%85%A6%E1%86%BA%E1%84%91%E1%85%B3%E1%86%AF%E1%84%85%E1%85%B5%E1%86%A8%E1%84%89%E1%85%B3%20%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%84%80%E1%85%B3%E1%84%85%E1%85%A2%E1%86%B7%20%E1%84%89%E1%85%A1%E1%86%BC%E1%84%8B%E1%85%A7%E1%86%BC%E1%84%89%E1%85%B5%E1%84%80%E1%85%A1%E1%86%AB%20%E1%84%92%E1%85%AA%E1%86%A8%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%92%E1%85%A1%E1%84%80%20b1645bc0778e4e42b86e4dc09e030403/Untitled.png)

## 답안2 - 영화

```python
netflix_rok_df['duration'].unique()
결과) array(['99 min', '1 Season', '107 min', '135 min', '2 Seasons', '133 min',
       '109 min', '137 min', '110 min', '140 min', '128 min', '102 min',
       '143 min', '118 min', '5 Seasons', '111 min', '63 min', '122 min',
       '4 Seasons', '123 min', '112 min', '139 min', '136 min', '91 min',
       '130 min', '116 min', '125 min', '100 min', '126 min', '3 Seasons',
       '54 min'], dtype=object)
```

```python
colors = ['lightslategray']
colors[0] = 'crimson'

movie_dur = pd.value_counts(netflix_rok_movies['duration'])
fig = go.Figure([go.Bar(x=movie_dur.index, y=movie_dur.values,
                        text=movie_dur.values, marker_color=colors)])
fig.update_traces(textposition='outside')
fig.update_layout(title='한국 영화 상영시간 분포도', xaxis={'categoryorder':'total descending'})

fig.show()
```

![%E1%84%92%E1%85%A1%E1%86%AB%E1%84%80%E1%85%AE%E1%86%A8%20%E1%84%82%E1%85%A6%E1%86%BA%E1%84%91%E1%85%B3%E1%86%AF%E1%84%85%E1%85%B5%E1%86%A8%E1%84%89%E1%85%B3%20%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%84%80%E1%85%B3%E1%84%85%E1%85%A2%E1%86%B7%20%E1%84%89%E1%85%A1%E1%86%BC%E1%84%8B%E1%85%A7%E1%86%BC%E1%84%89%E1%85%B5%E1%84%80%E1%85%A1%E1%86%AB%20%E1%84%92%E1%85%AA%E1%86%A8%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%92%E1%85%A1%E1%84%80%20b1645bc0778e4e42b86e4dc09e030403/Untitled%201.png](%E1%84%92%E1%85%A1%E1%86%AB%E1%84%80%E1%85%AE%E1%86%A8%20%E1%84%82%E1%85%A6%E1%86%BA%E1%84%91%E1%85%B3%E1%86%AF%E1%84%85%E1%85%B5%E1%86%A8%E1%84%89%E1%85%B3%20%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%84%80%E1%85%B3%E1%84%85%E1%85%A2%E1%86%B7%20%E1%84%89%E1%85%A1%E1%86%BC%E1%84%8B%E1%85%A7%E1%86%BC%E1%84%89%E1%85%B5%E1%84%80%E1%85%A1%E1%86%AB%20%E1%84%92%E1%85%AA%E1%86%A8%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%92%E1%85%A1%E1%84%80%20b1645bc0778e4e42b86e4dc09e030403/Untitled%201.png)