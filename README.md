# blogpost_task


git clone project

git clone https://github.com/uday99/blogpost_task.git



Install docker installer.exe


Docker version 20.10.17, build 100c701 



Install the packages and the pgadmin and postgres database from Dockerfile 

docker-compose build
docker-compose up
first create the build for postgres and pg admin in docker-compose.yml

open the browser with url:http://127.0.0.1:5050/browser/
pgadmin ui will appear 
enter username: pgadmin4
      password  admin1234



create the database server and the database in pgadmin4 with servername,host name, username,password and the database name

after the set up of pgadmin and postgres database compose the web app for the django

server: djangodb_demo

database:postgres
Username: postgres
password:1234

host :postgresql_database




In setting.py of django project  file


setup 

database name,hostname,servername,username in Database configuration


Install all the requiments of the Project using docker compose build
1.Build web app
2. It will install all the packages of  the Django,graphql

3.docker-compose up


django project server  runs

open the browser with 
127.0.0.1:8000/graphql





the graphql interface opens


Signup the user
================

mutation {
   register (
     email: "ravi@gmail.com",
     username: "ravi kumar",
     password1: "rkumar123@@",
     password2: "rkumar123@@"
   ) {
    
    
     success,
     errors,
     token,
     refreshToken,
   }
 }


login the user if the token expires 
=======================================


mutation {
  tokenAuth(username: "mainadmin", password: "blackbox") {
    success
    errors
    token
    refreshToken
  }
}



response:
{
  "data": {
    "tokenAuth": {
      "success": true,
      "errors": null,
      "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im1haW5hZG1pbiIsImV4cCI6MTY5MzMyMTIyOSwib3JpZ0lhdCI6MTY5MzMyMDkyOX0.HAH_xARTc3vtAGw_U31b1tyzHMI0W4UZlSOLNRXeSOc",
      "refreshToken": "c15e0f27e720110700098034277ca8cd87a28996"
    }
  }
}




userslist:
===========


query{
  userslist{
    id,
    username
    email
    createdAt
    updatedAt
  }
}




{
  "data": {
    "userslist": [
      {
        "id": "1",
        "username": "admin2",
        "email": "admin2@gmail.com",
        "createdAt": "2023-08-29T10:53:43.059547+00:00",
        "updatedAt": "2023-08-29T10:53:43.059547+00:00"
      },
      {
        "id": "2",
        "username": "udaykumarandolu",
        "email": "udaykumar123@gmail.com",
        "createdAt": "2023-08-29T10:57:13.193853+00:00",
        "updatedAt": "2023-08-29T10:57:13.193853+00:00"
      },
      {
        "id": "3",
        "username": "mainadmin",
        "email": "superuser123@gmail.com",
        "createdAt": "2023-08-29T11:03:14.425167+00:00",
        "updatedAt": "2023-08-29T11:03:14.425167+00:00"
      },
      {
        "id": "4",
        "username": "superadmin",
        "email": "superadmin12@gmail.com",
        "createdAt": "2023-08-29T11:43:17.461473+00:00",
        "updatedAt": "2023-08-29T11:43:17.461473+00:00"
      },
      {
        "id": "5",
        "username": "joseph",
        "email": "joseph12@gmail.com",
        "createdAt": "2023-08-30T08:42:43.247020+00:00",
        "updatedAt": "2023-08-30T08:42:43.247020+00:00"
      }
    ]
  }
}



read user

===============


query{
  userid(id:1){
    id
    username
    email
  }
}




{
  "data": {
    "userid": {
      "id": "1",
      "username": "admin2",
      "email": "admin2@gmail.com"
    }
  }
}










CRUD operations for post and comment pass the JWT token in Headers
====================================================================

{"Authorization":"JWT yJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im1haW5hZG1pbiIsImV4cCI6MTY5MzMyMTIyOSwib3JpZ0lhdCI6MTY5MzMyMDkyOX0.HAH_xARTc3vtAGw_U31b1tyzHMI0W4UZlSOLNRXeSOc"}






create post
=========


mutation {
  createPost(title: "Kalki", content: "the Movie ", authorIdId: 3) {
    success
    post {
      title
      content
      id
      createdAt
      updatedAt
    }
  }
}






{
  "data": {
    "createPost": {
      "success": true,
      "post": {
        "title": "Kalki",
        "content": "the Movie is directed by nagashwin and acted by prabhas ",
        "id": "4",
        "createdAt": "2023-08-30T11:54:17.885687+00:00",
        "updatedAt": "2023-08-30T11:54:17.885687+00:00"
      }
    }
  }
}



updatepost
=========

mutation {
  updatePost(title: "Hyderabad IT city",content: "National IT city is Hyderabad",id:6) {
    success
    post {
      title
      content
      id
      createdAt
      updatedAt
    }
  }
}


{
  "data": {
    "updatePost": {
      "success": true,
      "post": {
        "title": "Hyderabad IT city",
        "content": "National IT city is Hyderabad",
        "id": "6",
        "createdAt": "2023-08-30T12:14:07.681495+00:00",
        "updatedAt": "2023-08-30T13:16:18.245714+00:00"
      }
    }
  }
}






read post:
==========
query {
  readpost(id:2){
    
    id
    title
    content
    
    
    
  }
}



{
  "data": {
    "readpost": {
      "id": "2",
      "title": "Spider Man",
      "content": "the most famous comic action hero loved by kids"
    }
  }
}




list of blogposts
====================

query{
  blogposts{
    id
    authorId{
      username
      email
      updatedAt
      createdAt
    }
    title
    content
    createdAt
    updatedAt
    
    
    
    
  }
}




{
  "data": {
    "blogposts": [
      {
        "id": "1",
        "authorId": {
          "username": "mainadmin",
          "email": "superuser123@gmail.com",
          "updatedAt": "2023-08-29T11:03:14.425167+00:00",
          "createdAt": "2023-08-29T11:03:14.425167+00:00"
        },
        "title": "The Hindu",
        "content": "Its a Renowed newspaper",
        "createdAt": "2023-08-29T13:26:57.280129+00:00",
        "updatedAt": "2023-08-29T13:26:57.280129+00:00"
      },
      {
        "id": "2",
        "authorId": {
          "username": "mainadmin",
          "email": "superuser123@gmail.com",
          "updatedAt": "2023-08-29T11:03:14.425167+00:00",
          "createdAt": "2023-08-29T11:03:14.425167+00:00"
        },
        "title": "Spider Man",
        "content": "the most famous comic action hero loved by kids",
        "createdAt": "2023-08-29T13:31:33.808823+00:00",
        "updatedAt": "2023-08-29T13:31:33.808823+00:00"
      },
      {
        "id": "3",
        "authorId": {
          "username": "mainadmin",
          "email": "superuser123@gmail.com",
          "updatedAt": "2023-08-29T11:03:14.425167+00:00",
          "createdAt": "2023-08-29T11:03:14.425167+00:00"
        },
        "title": "Chandrayaan 3 by the ISRO",
        "content": "Isro has launched the chandrayan3 in low budget ",
        "createdAt": "2023-08-29T13:32:29.313269+00:00",
        "updatedAt": "2023-08-30T04:12:23.294715+00:00"
      }
    ]
  }
}



create post comment
=====================
mutation {
  createPostComment(
    postIdId: 10
    content: "Salman khar is famous bollywood actor and also role player"
    authorIdId: 1
  ) {
    success
    comment {
      content
      createdAt
      updatedAt
    }
  }
}



list of comments

query{
  comments{
    id
    postId{
      title
      content
    }
    content
    createdAt
    updatedAt
    authorId {
      id
    }
    
    
  }
}









{
  "data": {
    "comments": [
      {
        "id": "1",
        "postId": {
          "title": "Chandrayaan 3 by the ISRO",
          "content": "Isro has launched the chandrayan3 in low budget "
        },
        "content": "Its india honor launch the chandrayan 13",
        "createdAt": "2023-08-29T13:57:22.509764+00:00",
        "updatedAt": "2023-08-30T07:36:53.725630+00:00",
        "authorId": {
          "id": "3"
        }
      },
      {
        "id": "2",
        "postId": {
          "title": "Hyderabad IT city",
          "content": "National IT city is Hyderabad"
        },
        "content": "Though Hyd is national IT city its terrible in traffic",
        "createdAt": "2023-08-30T13:28:22.825167+00:00",
        "updatedAt": "2023-08-30T13:28:22.825167+00:00",
        "authorId": {
          "id": "5"
        }
      }
    ]
  }
}



read commentid:

===============

query{
  readcomment(id:1){
    id
    postId{
      title
      content
    }
    content
    createdAt
    updatedAt
    authorId {
      id
    }
    
    
  }
}

{
  "data": {
    "readcomment": {
      "id": "1",
      "postId": {
        "title": "Chandrayaan 3 by the ISRO",
        "content": "Isro has launched the chandrayan3 in low budget "
      },
      "content": "Its india honor launch the chandrayan 13",
      "createdAt": "2023-08-29T13:57:22.509764+00:00",
      "updatedAt": "2023-08-30T07:36:53.725630+00:00",
      "authorId": {
        "id": "3"
      }
    }
  }
}







update post comment
==================


  mutation {
  updatePostComment(content: "Though Hyd is national IT city its terrible in traffic and pollution",id:2) {
    success
    comment {
      
      content
      id
      createdAt
      updatedAt
      
      postId {
        id
      }
      
    }
  }
}




{
  "data": {
    "updatePostComment": {
      "success": true,
      "comment": {
        "content": "Though Hyd is national IT city its terrible in traffic and pollution",
        "id": "2",
        "createdAt": "2023-08-30T13:28:22.825167+00:00",
        "updatedAt": "2023-08-30T13:53:24.186277+00:00",
        "postId": {
          "id": "6"
        }
      }
    }
  }
}



Delete the post ,comment User

=========================
UserId deletes all the post comments,user 

mutation {
  delete(UserId:11){
    success
    error
  }
}


postId
=======
it deletes only the post ,comment

mutation {
  delete(postId:11){
    success
    error
  }
}


commentId
============


it deletes the comment


mutation {
  delete(commentId:11){
    success
    error
  }
}



























