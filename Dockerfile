FROM debian

RUN apt update && apt install -y \
curl \
less

RUN curl -o /tmp/jj.tar.gz https://release-assets.githubusercontent.com/github-production-release-asset/322484700/371de821-c5e6-47a5-8815-8026ae09ff8c?sp=r\&sv=2018-11-09\&sr=b\&spr=https\&se=2026-05-26T12%3A30%3A14Z\&rscd=attachment%3B+filename%3Djj-v0.41.0-aarch64-unknown-linux-musl.tar.gz\&rsct=application%2Foctet-stream\&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0\&sktid=398a6654-997b-47e9-b12b-9515b896b4de\&skt=2026-05-26T11%3A30%3A07Z\&ske=2026-05-26T12%3A30%3A14Z\&sks=b\&skv=2018-11-09\&sig=NBknLXb0B6l7J8Ty8%2B5FhTLn1oE9qGBinliaYL0PTEE%3D\&jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmVsZWFzZS1hc3NldHMuZ2l0aHVidXNlcmNvbnRlbnQuY29tIiwia2V5Ijoia2V5MSIsImV4cCI6MTc3OTc5NjE4MCwibmJmIjoxNzc5Nzk1ODgwLCJwYXRoIjoicmVsZWFzZWFzc2V0cHJvZHVjdGlvbi5ibG9iLmNvcmUud2luZG93cy5uZXQifQ.WaE-1MkdKynNgWMuaPQXmnJGDJrfIK6WyblEwDKYWZ0\&response-content-disposition=attachment%3B%20filename%3Djj-v0.41.0-aarch64-unknown-linux-musl.tar.gz\&response-content-type=application%2Foctet-stream \
&& cd /tmp \
&& tar -xzf /tmp/jj.tar.gz \
&& mv /tmp/jj /bin/


