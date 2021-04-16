# 한국 넷플릭스 장르별 비중은 어떻게 될까? 그래프로 확인해보자

## 학습목표

시각화 라이브러리 seaborn을 활용해 목적에 맞는 시각화하기

## 답안

2번에서 한국 Netflix 프로그램의 유형은 TV show와 Movie만 있다는 것을 확인했다. 
이 2가지 유형 별 비중을 그래프로 시각화 하려면 TV show에 대한 정보와 Movie에 대한 정보를 담은 데이터를 각각 변수로 지정하는 작업이 선행되어야 한다.

1. 한국 Netflix 프로그램 중 **TV Show**에 해당하는 데이터프레임을 생성하기

```python
netflix_rok_shows = netflix_rok_df[netflix_rok_df['type'] == 'TV Show']
netflix_rok_shows.head()
```

2. 한국 Netflix 프로그램 중 **Movie**에 해당하는 데이터프레임을 생성하기

```python
netflix_rok_movies = netflix_rok_df[netflix_rok_df['type'] == 'Movie']
netflix_rok_movies.head()
```

3. 시각화 단계

```python
# %matplotlib inline : notebook을 실행한 브라우저에서 바로 그래프를 볼 수 있게 함

%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
```

```markdown
f, ax = plt.subplots(figsize=(10, 6))
ax.set_title('넷플릭스 대한민국 한국 영화 VS. TV 프로그램', family='D2Coding', size=20)

plt.xkcd()

sns.set(style='whitegrid')
sns.countplot(data=netflix_rok_df, x='type', palette='pastel')
```

- 결과

![%E1%84%92%E1%85%A1%E1%86%AB%E1%84%80%E1%85%AE%E1%86%A8%20%E1%84%82%E1%85%A6%E1%86%BA%E1%84%91%E1%85%B3%E1%86%AF%E1%84%85%E1%85%B5%E1%86%A8%E1%84%89%E1%85%B3%20%E1%84%8C%E1%85%A1%E1%86%BC%E1%84%85%E1%85%B3%E1%84%87%E1%85%A7%E1%86%AF%20%E1%84%87%E1%85%B5%E1%84%8C%E1%85%AE%E1%86%BC%E1%84%8B%E1%85%B3%E1%86%AB%20%E1%84%8B%E1%85%A5%E1%84%84%E1%85%A5%E1%87%82%E1%84%80%E1%85%A6%20%E1%84%83%E1%85%AC%E1%86%AF%E1%84%81%E1%85%A1%20ad6fccfadfff461fb76adc0c629e83c1/Untitled.png](%E1%84%92%E1%85%A1%E1%86%AB%E1%84%80%E1%85%AE%E1%86%A8%20%E1%84%82%E1%85%A6%E1%86%BA%E1%84%91%E1%85%B3%E1%86%AF%E1%84%85%E1%85%B5%E1%86%A8%E1%84%89%E1%85%B3%20%E1%84%8C%E1%85%A1%E1%86%BC%E1%84%85%E1%85%B3%E1%84%87%E1%85%A7%E1%86%AF%20%E1%84%87%E1%85%B5%E1%84%8C%E1%85%AE%E1%86%BC%E1%84%8B%E1%85%B3%E1%86%AB%20%E1%84%8B%E1%85%A5%E1%84%84%E1%85%A5%E1%87%82%E1%84%80%E1%85%A6%20%E1%84%83%E1%85%AC%E1%86%AF%E1%84%81%E1%85%A1%20ad6fccfadfff461fb76adc0c629e83c1/Untitled.png)

## 사용된 코드

- dataframe.head() : 해당 데이터의 상단 5열을 출력한다. 5열은 default값이며 head안에 숫자를 넣으면 기입한 숫자 개수와 동일한 열의 개수가 출력된다.