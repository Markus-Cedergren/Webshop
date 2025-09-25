#Frontend based on alpine
FROM nginx:alpine

#Copy all the files to the specified location
COPY . /usr/share/nginx/html
#need to overwrite the nginx.conf, since I implement custom reverse proxy. 
COPY nginx.conf /etc/nginx/nginx.conf