# User stories
As a blogger
So I can write interesting stuff
I want to write posts having a title.

As a blogger
So I can write interesting stuff
I want to write posts having a content.

As a blogger
So I can let people comment on interesting stuff
I want to allow comments on my posts.

As a blogger
So I can let people comment on interesting stuff
I want the comments to have a content.

As a blogger
So I can let people comment on interesting stuff
I want the author to include their name in comments.

# Nouns:
Posts, title, content, comments, name.

# Records --- Properties
Posts         title, content
Comments      post, content, name

# Column types
Table: Posts
id: SERIAL
title: text
content: text

Table: Comments
id: SERIAL
content: text
name: text

Can a post have many comments ?

YES ! 

Can a comment have many posts ?

NO ! 

Therefore the commment belongs to the post and so the foreign id is in the comments table
