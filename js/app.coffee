#
# This is the main file for your application
# and is loaded by the application at launch

# get the spotify api and put it in the
# global object (for debugging) and locally
@sp = sp = getSpotifyApi()

models = sp.require('sp://import/scripts/api/models');

# main
main = document.getElementById("main")

mod = (fn) ->
        o = {}
        fn.apply(o)
        return o

@router = router = mod ->
        pages = default: -> console.warn "no-op path",arguments

        doRouting = (args) ->
                if args.length == 0
                        pages["default"]()
                        return

                cur = pages
                for i in [0..args.length]
                        if typeof cur is "function"
                                cur(args.splice(i))
                                return

                        # store the last default handler
                        if cur.hasOwnProperty "default"
                                def = cur["default"]

                        if cur.hasOwnProperty args[i]
                                cur = cur[args[i]]
                                continue
                        else
                                def(args.splice(i))
                                return

        changed = (ev) -> doRouting sp.core.getArguments()

        sp.core.addEventListener("argumentsChanged",changed)

        @addPage = (name,handler) ->
                pages[name] = handler
        @navigate = navigate = (path) ->

                if typeof path is "string"
                        navigate path.split(":")
                else
                        history.pushState(path)
                        doRouting(path)





@onFirstRun = ->
        console.log("first run!")
        @router.navigate("welcome")

@storage = (->

        @addEventListener "unload", =>
                @localStorage.main = JSON.stringify(@storage)

        callFirstRun = -> setTimeout @onFirstRun.bind(this)

        if @localStorage.main?
                o = JSON.parse(@localStorage.main)
                if o.forceFirstRun
                        @console.log("forced first run")
                        callFirstRun()
                        o.forceFirstRun = false

                return o
        else
                @localStorage["main"] = "{}"#store empty object
                callFirstRun()
                return {}
)()


router.addPage "welcome", (args) ->
        # We are probably want to check if this user is really new
        # with our server.
        cont = @document.createElement("div")

        (p = @document.createElement("p")).innerText = "Hello there"
        cont.appendChild p

        main.innerHtml = ""
        main.appendChild cont






