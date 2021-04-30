# howdoi-telegram

[Gleitz/howdoi](https://github.com/Infotelaz/howdoi-telegram) daxil olmaq üçün bir telegram botu. Ani kodlaşdırma cavablarını alın. Kodlaşdırma suallarınıza cavab verən Telegram bot.

Diqqəti yayındırmadan tez bir zamanda həll yolu tapın.

Bax!

![demo-gif](images/howdoi_0.01.gif)

## How to run

İstənilən OS-də işləyə bilərsiniz (windows / mac / linux). Daha yaxşı etibarlılıq üçün Digital Ocean Droplet kimi bir VPS yerləşdirə bilərsiniz. Termux tətbiqindən istifadə edərək hətta Android-də işləyə bilərsiniz.

Terminalı açın və botu işə salmaq üçün təlimatları izləyin.

- `git`, `python` and `pip` olduğundan əmin olun..

    ```bash
    # aşağıdakı əmrlər səhv yaratmamalıdır
    git --version
    python --version # 3.9 is recommended
    pip --version
    ```

    > **Qeyd:** Bəzi sistemlərdə `python` 3 versiyası` python3` kimi mövcuddur

- Hər şeydən əvvəl, anbarı klonlayın.

    ```shell
    git clone https://github.com/Infotelaz/howdoi-telegram.git
    ```

- İndi `howdoi-telegram` qovluğuna keçin.

    ```shell
    cd howdoi-telegram
    ```

- Bir piton virtual mühiti yaradın.

    ```bash
    python -m venv .venv # qurmaq
    source .venv/bin/activate # aktivləşdir (unix)
    # virtual mühiti aktivləşdirmək əmri Windows, google axtarışı üçün fərqlidir
    ```

## Deploy to Heroku

You can click this button to deploy to Heroku.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Infotelaz/howdoi-telegram)

For more details [read the guide](https://github.com/aahnik/howdoi-telegram/issues/6) about Heroku deployment.

<!-- deploy success -->

## Contributing

Issues and PRs welcome!
