FROM node:16.14.2

# Install Yarn

WORKDIR /front_code

# Install dependencies
COPY package.json /front_code
RUN yarn
ENV PATH $PATH:/front_code/node_modules/.bin

EXPOSE 3000
