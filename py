# Initial string containing poem details: title, author, and publication date
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(highlighted_poems)
# Split the string into a list of poem details
highlighted_poems_list = highlighted_poems.split(',')

# Initialize an empty list to store cleaned-up poem details
highlighted_poems_stripped = []

# Strip whitespace from each poem detail and add to the new list
for poem in highlighted_poems_list:
    highlighted_poems_stripped.append(poem.strip())
# Initialize an empty list to store lists of poem details
highlighted_poems_details = []

# Split each poem detail into title, author, and date, and add to the list
for poem in highlighted_poems_stripped:
    highlighted_poems_details.append(poem.split(':'))

# Initialize lists to store titles, poets, and dates separately
titles = []
poets = []
dates = []

# Extract titles, poets, and dates from the details and add to respective lists
for poem in highlighted_poems_details:
    titles.append(poem[0])
    poets.append(poem[1])
    dates.append(poem[2])
