file_name=input("File name:").strip().lower().split(".")[-1]
file_accordingto_name={
    "gif":"image/gif",
    "jpg":"image/jpeg",
    "png":"image/png",
    "pdf":"image.pdf",
    "txt":"text/plain",
    "zip":"application/zip"
}
print(file_accordingto_name[file_name])

