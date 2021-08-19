#!/bin/bash
# Request an action that causes the server to respond with "You got me!"
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" http://83c6c24932a4.f706bb2c.hbtn-cod.io:5000/catch_me_3
