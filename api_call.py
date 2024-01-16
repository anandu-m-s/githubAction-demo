import requests
import os
def main():
   api_url="http://localhost:8082/doc/demo/create/pkpzip"
   repo_name=os.getenv("INPUT_REPO_NAME")
   json_file_path=os.getenv("INPUT_JSON_FILE_PATH")

with open(json_file_path,"rb") as file:
  response= requests.post(
    api_url,
    headers={"Content-Type":"application/json"},
    data=file
  )

print(response.text)

if __name__ == "__main__":
  main()
