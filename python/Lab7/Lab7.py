import wikipedia

searchInput = input("Enter a value to search wikipedia for:")

searchResults = wikipedia.search(searchInput)
searchSuggestion =  wikipedia.suggest(searchInput)

print("-------------Search Results and Suggestion-----------")
print(searchResults)
print(searchSuggestion)

suggestSummary = wikipedia.summary(searchSuggestion)

print("-------------Suggestion Summary-----------")
print(suggestSummary)

page = wikipedia.page(searchSuggestion)
print("-------------Page Data-----------")
print(page.url)
print(page.title)
print(page.content)
