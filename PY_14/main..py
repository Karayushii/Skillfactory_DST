thresh = df.shape[0]*0.5
df = df.dropna(how='any',thresh=thresh,axis = 1)
thresh_2= df.shape[1]-2
df = df.dropna(how='any',thresh=thresh_2,axis=0)
values={
    'one':df['one'].mean(),
    'two':df['two'].mean(),
    'three':df['three'].mean(),
    'four':df['four'].mode()[0]
}
df = df.fillna(values)
