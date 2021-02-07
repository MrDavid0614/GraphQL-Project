FROM node:12.18.3-alpine as node
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

FROM nginx
COPY --from=node /app/dist/learningAngular /usr/share/nginx/html
EXPOSE 4200
CMD ["nginx", "-g", "daemon off;"]