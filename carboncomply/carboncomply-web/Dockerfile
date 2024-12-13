# build environment
FROM node:22-alpine as build

ARG API_URL

ENV PATH /node_modules/.bin:$PATH
COPY package.json ./
COPY package-lock.json ./
RUN npm ci 
RUN npm install react-scripts@3.4.1 -g --silent
COPY . ./
RUN REACT_APP_API_URL=${API_URL} npm run build

# production environment
FROM nginx:stable-alpine
COPY nginx_conf/default.conf /etc/nginx/conf.d/default.conf
COPY --from=build /build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

