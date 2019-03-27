import File_Searcher
file_found,folder=File_searcher.Search("my resume","D:/","doc") # you should use different string name to search
if file_found is not None:
  print("your file found: ",file_found)
else:
  print("file not found")
