import media
import movie_trailer


# Movie class의 instnace(object) 생성
sen_chiro = media.Movie("센과 치히로의 행방불명",
                        "トンネルのむこうは、不思議な町でした。\n터널의 저편은, 신비한 마을이었습니다.",
                        "https://w.namu.la/s/cc663b8090b99152852a73aa5a4712ffe57495786e2d307beb96dad17fead873fa10b43ccd6908adb71cca1ef31aa5fdbf381f1b2db2da46909e0404baa9c0a51ef32a328aec9bc4ff01c555a9f55de89dd08209c98add461d063b7a4d508149108f1b8c3db4bbe6aca829420c39bcb5",
                        "https://youtu.be/lwrG3HQXTFw")

your_name = media.Movie("너의 이름은",
                     "아직 만난 적 없는 너를, 찾고 있어.\nまだ会ったことのない君を、探している",
                    "https://w.namu.la/s/c3d26ed9926fe8427c0145842b0ad15021c3fc5b9afaf2ce78eac7d023239215d4fba997a1a025a30687669f35f4063adcb2e97762dc0b948cf352edae94039846c65a507af058c0cf40e15a0bf0db49571bb902f895abb3d9061df7917e22dda008b89deb7cd432c7a73a747d2073b2",
                    "https://www.youtube.com/watch?v=enRm-9qF2L8")

about_time = media.Movie("어바웃 타임",
                        "어떠한 순간을 다시 살게 된다면, 과연 완벽한 사랑을 이룰 수 있을까?",
                        "https://ww.namu.la/s/38024799ef91fd1a3e54e96b037188bacd36dd3b17c99ad5c9d934610750e86a1c3659725ec1c8f506259c6e396ca02b868bd6bac4bc6f3e1dc5ef5fe162756cddd57b9ec5c5db8bb80c50b69673dc2e7f7ddced19d8f876722cb2244ef8be79c8efedda9c9b8bcc4871afd8f2833f61",
                        "https://www.youtube.com/watch?v=T7A810duHvw")

totoro = media.Movie("이웃집 토토로",
                        "이 이상한 생물은, 아직 일본에 있답니다.",
                        "https://w.namu.la/s/3d05a85958eae3318f813157fa4b8d6bcd8dad23bbf043276c11a48097fa81ee20980d25731d811acf8ef2824bb5d0d6e75390536eec6771dfab45c6c855db5341a95b8307370e3f5d82351b0f64f3321403f6ba58b6e0abc2a10ec90092a467",
                        "https://www.youtube.com/watch?v=yrqmx630BIA")

twilight = media.Movie("트와일라잇",
                        "얼음보다 차갑고 빛보다 빠른 그가 온다!",
                        "http://t1.daumcdn.net/movie/cfd7acab60c34738a9b8cb5d012885871542171250906",
                        "https://www.youtube.com/watch?v=e8lynTVeKYU")

lala_land = media.Movie("라라랜드",
                        "황홀한 사랑, 순수한 희망, 격렬한 열정… 이 곳에서 모든 감정이 폭발한다!",
                        "https://ww.namu.la/s/d5720251d4891bccdf71bf5af160d9b691462069da28c63cb286cb5f3c8513a1c6a488bbbcefca6931cf7fedd0ee6365d55c4b2e3a1df72156f692987829918b81334ee0c75604ecc4f6d4df7dee6366779524a0e63b2e90d30a665bd5f02bf4",
                        "https://www.youtube.com/watch?v=Dt5hFexM5BI")

little_forest = media.Movie("리틀 포레스트",
                        "고단한 도시의 삶에 지쳐 고향으로 내려온 혜원이 소꿉친구인 재하와 은숙을 만나고 사계절의 자연 속에서 직접 만든 음식을 통해 과거의 기억과 상처를 치유해 나가는 힐링 드라마. ",
                        "https://w.namu.la/s/a178efcd163eb778aaf1a4db47dd8fee55990b4c8dcb258d2ec7406618e412ac2f3fb17a41a8328cf4956f04381d93d14db8b7a3dfe75c7d651ad39d460117138a0902b806117b9da3da9e80ff7a1ac765fe9833fe73125937fd181909ee2b4b14de02e70abf87a89213a97bfe63b534",
                        "https://www.youtube.com/watch?v=2h_bZfp8QNc")

movies = [sen_chiro, your_name, about_time, totoro, twilight, lala_land, little_forest]

movie_trailer.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)