## firebase initialize document
https://firebase.google.com/docs/admin/setup


## 環境起動 Dockerコンテナ内で
```
python3 backend/manage.py runserver 0.0.0.0:8000

```

## Django のインストール

```
pip install Django==3.2

```

## package のインストール

```
pip install -r requirements.txt
python3 -m pip freeze > requirements.txt
```


## Django コマンド

```
#.付けないで作成する事


django-admin startproject <googlemaptest> 

<!-- プロジェクトへ移動してからappを作成しないとエラーになる。 -->
$ cd googlemaptest
$ python3 manage.py startapp mapapp 


#maigration
python3 manage.py migrate
```

## 必須パッケージ

- autopep8 フォーマッター
- typing 型付け
- firebase_admin
- googlemaps

## GOOGLE MAP DOCUMENT
https://developers.google.com/maps/documentation/javascript/adding-a-google-map?hl=ja#maps_add_map-html


{% comment %} $.ajax({
 url: url,
 type: "POST",
 data: {
 polygon: polygonCoords,
 },success: function (result) {
 alert("firebaseに保存しました");
 }
 }); {% endcomment %}

     submitButton.addEventListener("click", (event) => {
      console.log("click");
        
      {% autoescape off %}
      const url = "{% url 'mapapp:polygon-page' %}";
      {% endautoescape %}
     
     
    }
      
    console.log("polygonCoords is =>", polygonCoords);
    console.log("polygon is =>", polygon);