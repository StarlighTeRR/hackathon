#
<h1 align="center">Привет, меня зовут Имя
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>

# Проект
<p><font color="blue">Этот репозиторий используется для выполнение задания</font></p>

## Правила именования

### Ветви
`develop` Ветка разработки (она основная)

`features/n_taskname` Ветки для разработки новых функций. Они создаются от develop и сливаются обратно в develop после завершения работы над функцией.

`learn/n_name` Изучение чего-либо

`fixes/n_name` Исправление ошибок, найденных тестировщиками или пользователями

`hotfixes/name` Ветки для исправления критических багов в релизной версии. Создаются от main и после исправления сливаются в master и develop.

<p><font color="blue">Примеры</font></p>

`features/2_learn_pull_requests `

`features/14_add_discounts_to_customer`

`features/67_fix_validation_on_customer_pag`

### pullrequest
`N type(location):taskdescription`

`N` – номер задачи, отправляемой на проверку. Если несколько задач, то перечислите их через запятую.

`type` – тип решенной задачи – feature, fix, codestyle, ui, ci, refactor.

`location` – название класса, проекта или файла, которого коснулись ключевые 
изменения в запросе.

`taskdescription` – краткое описание задачи на русском языке.

<p><font color="blue">Примеры</font></p>

`10 feature(customer): добавлена валидация данных пользователя`

`27 fix(order): добавлены зарезервированные ID для уникальных заказов`

`55 codestyle(Model): исправлены грамматические ошибки в проекте  бизнес-логики, добавлены недостающие комментарии`

### Коммиты
| Название | Описание                                                        |
|----------|-----------------------------------------------------------------|
| build	   | Сборка проекта или изменения внешних зависимостей               |
| sec      | Безопасность, уязвимости                                        |
| ci       | Настройка CI и работа со скриптами                              |
| docs	   | Обновление документации                                         |
| feat	   | Добавление нового функционала                                   |
| fix	   | Исправление ошибок                                              |
| perf	   | Изменения направленные на улучшение производительности          |
| refactor | Правки кода без исправления ошибок или добавления новых функций |
| revert   | Откат на предыдущие коммиты                                     |
| style	   | Правки по кодстайлу (табы, отступы, точки, запятые и т.д.)      |
| test	   | Добавление тестов                                               |

<тип>(<область>): <описание изменения>

<пустая линия>

[необязательное тело]

<пустая линия>

[необязательный нижний колонтитул]

```
<тип>(<область>): <описание изменения>
  │       │             │
  │       │             └─⫸ Краткое изложение в настоящем времени. Без заглавной буквы. Без точки в конце.
  │       │
  │       └─⫸ Область коммита: animations|bazel|benchpress|common|compiler|compiler-cli|core|
  │                          elements|forms|http|language-service|localize|platform-browser|
  │                          platform-browser-dynamic|platform-server|router|service-worker|
  │                          upgrade|zone.js|packaging|changelog|docs-infra|migrations|ngcc|ve|
  │                          devtools|sln
  │
  └─⫸ Тип коммита: build|ci|docs|feat|fix|perf|refactor|test
```


<p><font color="blue">Примеры</font></p>

`docs(changelog): обновлён список изменений для beta.5`

`fix(release): Добавлены зависимости для последних версий rxjs и zone.js`

### Отличия слияний веток
![squash, rebase, merge](https://github.com/sergey69934/Programming/assets/124598976/71f4e98c-8cfd-4a8b-ac3a-a55a6aadb500)


## Дата последнего изменения
1-03-2024
