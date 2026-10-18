import game

words = game.load_words()

while game.has_words(words):
    word = game.pick_word(words)
    description = game.get_description(words, word)
    game.remove_word(words, word)
    table = game.create_table(word)
    lives = game.get_lives()

    while game.is_alive(lives):
        game.show_table(table)
        game.show_description(description)
        answer = game.prompt_answer()

        if game.is_word_correct(word, answer):
            table = game.open_word(word)
            game.show_table(table)
            game.show_win()
            break
        elif game.is_right_letter(word, answer):
            table = game.open_letter(table, word, answer)
            if game.is_table_complete(table):
                game.show_table(table)
                game.show_win()
                break
        else:
            game.show_wrong()
            lives = game.decrease_lives(lives)
            game.show_gallows(lives)
    else:
        game.show_lose(word)

    if game.has_words(words):
        replay = game.prompt_replay()
        if not game.is_yes(replay):
            break

game.show_finish(words)