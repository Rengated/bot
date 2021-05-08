import vk_api, time

vk_session = vk_api.VkApi('+79627460408', 'oroboz13')
vk_session.auth()

vk = vk_session.get_api()


zxc = 1000
while zxc > 0:
    time.sleep(3)
    vk.status.set(text='{} - 7 = {}'.format(zxc, zxc - 7))
    zxc -= 7
    if zxc < 50:
        zxc = 1000
