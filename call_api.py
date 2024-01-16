import requests
import os
def main():
   print("Hello World")
   api_url="http://localhost:8082/doc/demo/create/pkpzip"
   repo_name = sys.argv[1]
   json_file_path = sys.argv[2]
   # repo_name=os.getenv("INPUT_REPO_NAME")
   # json_file_path=os.getenv("INPUT_JSON_FILE_PATH")

# with open(json_file_path,"rb") as file:
#   response= requests.post(
#     api_url,
#     headers={"Content-Type":"application/json"},
#     data=file
#   )

print(api_url)

if __name__ == "__main__":
  main()
