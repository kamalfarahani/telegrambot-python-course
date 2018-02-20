from telegram.ext import Updater


def one_time_message(bot, job):
    bot.send_message(
        chat_id='ID', text='Once')


def repeating_message(bot, job):
    bot.send_message(
        chat_id='ID', text='Repeating')


def increasing_message(bot, job):
    if job.interval <= 10:
        bot.send_message(
            chat_id='ID', text=str(job.interval))

    job.interval += 1
    if job.interval > 10:
        job.schedule_removal()


def main():
    updater = Updater(token='TOKEN')

    job_queue = updater.job_queue

    job_queue.run_once(one_time_message, 1)
    job_queue.run_repeating(repeating_message, interval=10, first=15)
    job_queue.run_repeating(increasing_message, interval=1, first=2)

    updater.start_polling()


if __name__ == '__main__':
    main()
