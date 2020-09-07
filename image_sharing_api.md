# Api routes for an Image Sharing Application
The application url is taken as `https://image_share.com/`
## Links
1. [Create User](#create-user)
2. [Get all Users](#get-all-users)
3. [Get users by id](#get-user-by-id)
4. [Update user by id](#update-user-by-id)
5. [Delete user by id](#delete-user-by-id)
6. [Create post](#create-post)
7. [Get all posts for user](#get-all-posts-for-user)
8. [Get posts by id](#get-post-by-id)
9. [Update post by id](#update-post-by-id)
10. [Delete post by id](#delete-post-by-id)
11. [Like Post](#like-post)
12. [DataBase Structure](#database-structure)

# User Route
## Create user

`POST https://image_share.com/user/`

cURL
```
curl --location --request POST 'https://image_share.com/user/
--header 'Content-Type: application/json' \
--data-raw '{
    "user_name"  : "user"
}'
```

### Request Body
```json
{
    "user_name"  : "user"
}
```

### Response  if username is already taken

```json
{
    "error": "username already exists",
}
```

`Status : 500 ERROR`

### Response
```json
{
    "message": "User has been created",
    "details": {
        "user_id" : <randomly generated>,
        "user_name": "user",
        "no_of_pics" : 0
    }
}
```

`Status : 201 Created`



## Get all users

`GET https://image_share.com/users/`

cURL

```
curl --location --request GET 'https://image_share.com/users/'
```

### Response if there are no users
```json
{
    "message": "No users exist"
}
```
`Status : 404 NOT FOUND`

### Response if users exist
```json
{
    "message": " 3 Users Found",
    "Users" : [
        "data" : {
            "user_id" : "1b2h1b2h1k3o",
            "user_name" : "xyz",
            "no_of_pics" : 20
        }
        "data" : {
            "user_id" : "1b2h1b2h1k5o",
            "user_name" : "xqz",
            "no_of_pics" : 10
        }
        "data" : {
            "user_id" :"1b2h1b2h1k7o",
            "user_name" : "abc",
            "no_of_pics" : 15
        }
    ]
}
```
`Status : 200 OK`

## Get user by id


`GET https://image_share.com/user/<user_id>`

cURL 

```
curl --location --request GET 'https://image_share.com/users/<user_id>'
```

### Response if the user does not exist
```json
{
    "message": "User with id <user_id> does not exist"
}
```
`Status : 404 NOT FOUND`
### Response if the user exists
```json
{
    "message": "User Found",
    "data" : {
        "user_id" : <user_id>,
        "user_name" : "xyz",
        "no_of_pics" : 20
    }
}
```
`Status : 200 OK`



## Update user by id
`PATCH https://image_share.com/user/<user_id>`

cURL
```
curl --location --request PATCH 'https://image_share.com/user/<user_id>
--header 'Content-Type: application/json' \
--data-raw '[
    {
        "keyName" : "user_name",
        "value" : "updated_user_name"
    }
]'
```

### Request Body
```json
    {
        "keyName" : "user_name",
        "value" : "updated_user_name"
    }
```
### Response if the user does not exist
```json
{
    "message": "User with id <user_id> does not exist"
}
```
`Status : 404 NOT FOUND`

### Response
```json
{
    "message": "User Updated",
    "details": {
        "user_id" : <user_id>,
        "user_name": "updated_user_name",
        "no_of_pics" : 0
    }
}
```
`Status : 200 OK`



## Delete user by id

`DELETE https://image_share.com/user/<user_id>`

cURL
```
curl --location --request DELETE 'https://image_share.com/user/<user_id>'
```
### Response if the user does not exist
```json
{
    "message": "User with id <user_id> does not exist"
}
```
`Status : 404 NOT FOUND`
### Response
```json
{
    "message": "User Deleted",
    "deleted_user_id": "<user_id>"
}
```
`Status : 200 OK`




# Posts Route

## Create Post

`POST https://image_share.com/post/<user_id>`

cURL
```
curl --location --request POST 'https://image_share.com/post/<user_id>
--header 'Content-Type: application/json' \
--data-raw '{
    "image"  : <BINARY FILE>,
    "caption" : "Hello"
}'
```

### Request Body
```json
{
    "image"  : <BINARY FILE>,
    "caption" : "Hello"
}
```



### Response
```json
{
    "message": "Picture has been posted",
    "details": {
        "post_id" : <randomly generated>,
        "user_id": <user_id>,
        "caption" : "Hello",
        "likes" : 0
    }
}
```
`Status : 200 OK`

## Get all posts for user

`GET https://image_share.com/all_posts/<user_id>`

cURL

```
curl --location --request GET 'https://image_share.com/all_posts/<user_id>'
```
### Response if there is no user under the id
```json
{
    "message": "user doesnt exist"
}
```
`Status : 404 NOT FOUND`

### Response if there are no posts for user
```json
{
    "message": "No posts exist"
}
```
`Status : 404 NOT FOUND`

### Response if posts exist
```json
{
    "message": " 3 posts Found for <user_id>",
    "Posts" : [
        "details": {
            "post_id" : "1b2h1b2h1k3o",
            "user_id": <user_id>,
            "caption" : "Hello",
            "likes" : 12
        }
        "details": {
            "post_id" : "1b2h1b2h1k32o",
            "user_id": <user_id>,
            "caption" : "Helloow",
            "likes" : 2
        }
        "details": {
            "post_id" : "1b2h1b2h1k32t",
            "user_id": <user_id>,
            "caption" : "Hello2",
            "likes" : 23
        }
    ]
}
```
`Status : 200 OK`

## Get post by id


`GET https://image_share.com/post/<post_id>`

cURL 

```
curl --location --request GET 'https://image_share.com/posts/<post_id>'
```

### Response if the post does not exist
```json
{
    "message": "post with id <post_id> does not exist"
}
```
`Status : 404 NOT FOUND`
### Response if the post exists
```json
{
    "message": "post Found",
    "data" : {
        "post_id" : <post_id>,
        "user_id": <user_id>,
        "caption" : "Hello2",
        "likes" : 23
    }
}
```
`Status : 200 OK`

## Update post by id
`PATCH https://image_share.com/post/<post_id>`

cURL
```
curl --location --request PATCH 'https://image_share.com/post/<post_id>
--header 'Content-Type: application/json' \
--data-raw '[
    {
        "keyName" : "caption",
        "value" : "updated_caption"
    }
]'
```

### Request Body
```json
    {
        "keyName" : "caption",
        "value" : "updated_caption"
    }
```
### Response if the post does not exist
```json
{
    "message": "post with id <post_id> does not exist"
}
```
`Status : 404 NOT FOUND`

### Response
```json
{
    "message": "post Updated",
    "details": {
        "post_id" : <post_id>,
        "user_id": "aksj23kajsd",
        "caption": "updated_caption"
        "likes" : 23,

    }
}
```
`Status : 200 OK`

## Delete post by id

`DELETE https://image_share.com/post/<post_id>`

cURL
```
curl --location --request DELETE 'https://image_share.com/post/<post_id>'
```

### Response if the post does not exist
```json
{
    "message": "post with id <post_id> does not exist"
}
```
`Status : 404 NOT FOUND`

### Response
```json
{
    "message": "post Deleted",
    "deleted_post_id": "<post_id>"
}
```
`Status : 200 OK`


## Like Post

`PATCH https://image_share.com/post/like_post/<post_id>`

cURL
```
curl --location --request PATCH 'https://image_share.com/post/like_post/<post_id>
--header 'Content-Type: application/json' \
--data-raw '[
    {
        "$inc": {
            "likes": "1"
            }
    }
]'
```

### Request Body
```json
    {
        "$inc": {
            "likes": "1"
            }
    }
```
### Response if the post does not exist
```json
{
    "message": "post does not exist"
}
```
`Status : 404 NOT FOUND`

### Response
```json
{
    "message": "post Liked",
    "details": {
        "post_id" : <post_id>,
        "likes" : 24,
        "caption": "updated_caption"
    }
}
```
`Status : 200 OK`

# Database structure
`USERS`
```
user_id : int PRIMARY KEY,
user_name : string NOT NULL,
```
`POSTS`
```
posts_id : int PRIMARY KEY,
likes : int NOT NULL,
caption : String ,
FOREIGN KEY (user_id) REFERENCES USERS(user_id)
```
