import File_Searcher
file_found=File_searcher.Search("my resume","D:/","doc")
if file_found is not None:
  print("your file found: ",file_found)
else:
  print("file not found")
