#Import Library: Start by importing a library called urllib.request and give it a shorter name urllib for convenience.
import urllib.request as urllib

def main(url):
  print("Checking connectivity.")
  #Use urllib.urlopen(url) to try connecting to the provided URL.
  response = urllib.urlopen(url)
  #Print a message indicating successful connection along with the URL.
  print("Connected to ", url, "successfully")
  #Print the response code received from the connection.
  print("The response code was ", response.getcode())

print("This is a site connectivity checker program.")
#Take User Input: Use input() to get a URL from the user. Prompt them with "Input the URL of the site you want to check."
input_url = input("Input the URL of the site you want to check.")
#Call Main Function: Call the main() function and pass the user-provided URL as an argument.
main(input_url)