# WordPlay
Its a streamlit app used to play with pretrained word2vec models and try out different word analogies.
It uses gensim downloader API which extracts this vector directly from their sources.
List of available models and corpuses can be found here - [Gensim Downloader API](https://github.com/RaRe-Technologies/gensim-data)

![Screenshot](https://github.com/havingfun/WordPlay/blob/master/references/screenshot.png)

## How to Run

## With Docker
Build docker image
```
docker build . -t wordplayapp:latest
```
Run build image
```
docker run -p 8502:8502 wordplayapp
```
Project will be running on
```
http://localhost:8502/
```

## Without Docker
Install the requirements
```
pip install -r requirements.txt
```
Go to the streamlit directory
```
cd streamlit
```
Run streamlit app
```
streamlit run app.py --server.port 8502
```
Project will be running on
```
http://localhost:8502/
```
Incase your firewall is enabled, you will have to allow your system to open default streamlit port 8502 by doing
```
ufw allow 8502
```
