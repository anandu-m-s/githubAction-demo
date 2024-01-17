import requests
import os
import sys
def main():
   print("Hello World")
   # api_url="http://localhost:8082/doc/demo/create/pkpzip"
   
   # json_file_path=os.getenv("INPUT_JSON_FILE_PATH")
   # print(api_url)
   # print(json_file_path)

   # with open('pkp.json',"rb") as file:
   #   response= requests.post(
   #   api_url,
   #   headers={"Content-Type":"application/json"},
   #   data=file
   # )
   url="https://jsonplaceholder.typicode.com/todos"
   r= requests.get(url)
   print(r)

if __name__ == "__main__":
  main()
