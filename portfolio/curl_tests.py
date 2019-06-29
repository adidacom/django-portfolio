"""
djangoframework-jwt JSON web token testing
Generating a token:
curl -X POST -d "username=<username>&password=<password>" http://localhost:8000/api/auth/token/

token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Ind0cmFuIiwiZXhwIjoxNTQ4MDMyMjc4LCJlbWFpbCI6IiJ9.wTf9VnZekmrU_JoAJcFO8m9XDx8UgJpkP9jp6apPqKE

To access protected api:
curl -H "Authorization: JWT <your_token>" http://localhost:8000/protected-url/

Ex. Accessing comments api
curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Ind0cmFuIiwiZXhwIjoxNTQ4MDM0NTcxLCJlbWFpbCI6IiJ9.RvKqE79dNj2aJmxh1M7ufvtmZKyARkRQgTwIzGSwNwQ" http://localhost:8000/api/comments/


Ex. Creating comments api
curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Ind0cmFuIiwiZXhwIjoxNTQ4MDM1OTA2LCJlbWFpbCI6IiJ9.xa5EO57suRdcVIqocFEoiiLxpc8gLCg1U_kRQ8__WpY" -H "Content-Type: application/json" -d '{"content":"comment from curl"}'  'http://localhost:8000/api/comments/create/?slug=another-one&type=blog'

Ex. Creating child comments api
curl -X POST -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6Imd1ZXN0IiwiZXhwIjoxNTQ4MDM2NDA3LCJlbWFpbCI6IiJ9.aLZbraYxv8LllMuC8356l349U5OE1Ss8QEkp5U0qJdM" -H "Content-Type: application/json" -d '{"content":"guest reply to curl comment"}'  'http://localhost:8000/api/comments/create/?slug=another-one&type=blog&parent_id=44'

"""