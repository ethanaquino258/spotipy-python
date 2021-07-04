# create a function that reads genreSorter.csv and outputs all songs/uris that contain specific genre or subgenre ie contains 'pop' xxxxx
# display all possible genres to user (maybe too much?), take input string for filter xxxx
import pandas as pd

songs = pd.read_csv("user-library.csv")

# print(songs)

df = pd.DataFrame(data=songs)

desiredGenre = input("\nPlease enter the name of the genre you'd like to filter for:\n")

rslt_df = df.loc[df['genres'].str.contains(desiredGenre)]

print(rslt_df)
print(len(rslt_df))

if len(rslt_df) < 1:
    print("\ngenre not found!\n")
    exit

uriList = []

for index, row in rslt_df.iterrows():
    uriList.append(row['uri'])

# print(len(uriList))