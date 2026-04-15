@app.route("/ulsan-weather", methods=["GET", "POST"])
def ulsan_weather_skill():
    try:
        context = ssl._create_unverified_context()
        url = "https://search.naver.com/search.naver?query=%EC%9A%B8%EC%82%B0%20%EB%82%A0%EC%94%A8"

        webpage = urllib.request.urlopen(url, context=context)
        soup = BeautifulSoup(webpage, "html.parser")

        temps = soup.find("div", class_="temperature_text")
        summary = soup.find("p", class_="summary")

        if temps and summary:
            result_text = "울산 " + temps.get_text(strip=True) + " " + summary.get_text(strip=True)
        else:
            result_text = "날씨 정보를 가져오지 못했습니다."

    except Exception as e:
        result_text = f"날씨 조회 중 오류가 발생했습니다: {str(e)}"

    response = {
        "version": "2.0",
        "template": {
            "outputs": [{
                "simpleText": {
                    "text": result_text[:1000]
                }
            }]
        }
    }
    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

