FROM node:12.18.3-alpine as node
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

FROM nginx
EXPOSE 80
COPY --from=node /app/dist/learningAngular /usr/share/nginx/html
CMD [ "nginx", "-g", "daemon off;" ]