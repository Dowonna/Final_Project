# 한국 넷플릭스 프로그램 관람등급 확인하기

## 추가 문제 설명

한국 넷플릭스 TV프로그램, 영화의 관람등급은 어떻게 될까? 시각화해보자

### 학습목표

목적에 맞게 시각화하기

## 답안1 - TV 프로그램

```python
netflix_rok_shows['rating'].unique()
결과) array(['TV-14', 'TV-PG', 'TV-MA', 'TV-Y7', 'TV-Y', 'TV-G'], dtype=object)
```

```python
f, ax = plt.subplots(figsize=(10, 6))
ax.set_title('넷플릭스 대한민국 한국 TV 프로그램 영상물 등급', family='D2Coding', size=20)

plt.xkcd()
    
sns.set(style = "whitegrid")
sns.countplot(data=netflix_rok_shows, x='rating', palette='pastel',
             order=netflix_rok_shows['rating'].value_counts().index[0:])
```

![%E1%84%92%E1%85%A1%E1%86%AB%E1%84%80%E1%85%AE%E1%86%A8%20%E1%84%82%E1%85%A6%E1%86%BA%E1%84%91%E1%85%B3%E1%86%AF%E1%84%85%E1%85%B5%E1%86%A8%E1%84%89%E1%85%B3%20%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%84%80%E1%85%B3%E1%84%85%E1%85%A2%E1%86%B7%20%E1%84%80%E1%85%AA%E1%86%AB%E1%84%85%E1%85%A1%E1%86%B7%E1%84%83%E1%85%B3%E1%86%BC%E1%84%80%E1%85%B3%E1%86%B8%20%E1%84%92%E1%85%AA%E1%86%A8%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%92%E1%85%A1%2003faf88f02114a2dbf56a11da0731260/Untitled.png](%E1%84%92%E1%85%A1%E1%86%AB%E1%84%80%E1%85%AE%E1%86%A8%20%E1%84%82%E1%85%A6%E1%86%BA%E1%84%91%E1%85%B3%E1%86%AF%E1%84%85%E1%85%B5%E1%86%A8%E1%84%89%E1%85%B3%20%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%84%80%E1%85%B3%E1%84%85%E1%85%A2%E1%86%B7%20%E1%84%80%E1%85%AA%E1%86%AB%E1%84%85%E1%85%A1%E1%86%B7%E1%84%83%E1%85%B3%E1%86%BC%E1%84%80%E1%85%B3%E1%86%B8%20%E1%84%92%E1%85%AA%E1%86%A8%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%92%E1%85%A1%2003faf88f02114a2dbf56a11da0731260/Untitled.png)

## 답안2 - 영화

```python
netflix_rok_movies['rating'].unique()
결과) array(['TV-MA', 'TV-PG', 'NR', 'TV-14', 'TV-Y7'], dtype=object)
```

```python
f, ax = plt.subplots(figsize=(10, 6))
ax.set_title('넷플릭스 대한민국 한국 영화 영상물 등급', family='D2Coding', size=20)

plt.xkcd()
    
sns.set(style = "whitegrid")
sns.countplot(data=netflix_rok_movies, x='rating', palette='husl',
             order=netflix_rok_movies['rating'].value_counts().index[0:])
```

![%E1%84%92%E1%85%A1%E1%86%AB%E1%84%80%E1%85%AE%E1%86%A8%20%E1%84%82%E1%85%A6%E1%86%BA%E1%84%91%E1%85%B3%E1%86%AF%E1%84%85%E1%85%B5%E1%86%A8%E1%84%89%E1%85%B3%20%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%84%80%E1%85%B3%E1%84%85%E1%85%A2%E1%86%B7%20%E1%84%80%E1%85%AA%E1%86%AB%E1%84%85%E1%85%A1%E1%86%B7%E1%84%83%E1%85%B3%E1%86%BC%E1%84%80%E1%85%B3%E1%86%B8%20%E1%84%92%E1%85%AA%E1%86%A8%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%92%E1%85%A1%2003faf88f02114a2dbf56a11da0731260/Untitled%201.png](%E1%84%92%E1%85%A1%E1%86%AB%E1%84%80%E1%85%AE%E1%86%A8%20%E1%84%82%E1%85%A6%E1%86%BA%E1%84%91%E1%85%B3%E1%86%AF%E1%84%85%E1%85%B5%E1%86%A8%E1%84%89%E1%85%B3%20%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%84%80%E1%85%B3%E1%84%85%E1%85%A2%E1%86%B7%20%E1%84%80%E1%85%AA%E1%86%AB%E1%84%85%E1%85%A1%E1%86%B7%E1%84%83%E1%85%B3%E1%86%BC%E1%84%80%E1%85%B3%E1%86%B8%20%E1%84%92%E1%85%AA%E1%86%A8%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%92%E1%85%A1%2003faf88f02114a2dbf56a11da0731260/Untitled%201.png)