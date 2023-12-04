from fastapi import APIRouter
from api.prefectures import *
from api.japan_facts import *
import random


router = APIRouter()


@router.get('/japan')
def get_japan():
    return japan

@router.get('/hokkaido')
def get_hokkaido():
    return hokkaido

@router.get('/aomori')
def get_aomori():
    return aomori

@router.get('/iwate')
def get_iwate():
    return iwate

@router.get('/miyagi')
def get_miyagi():
    return miyagi

@router.get('/akita')
def get_akita():
    return akita

@router.get('/yamagata')
def get_yamagata():
    return yamagata

@router.get('/fukushima')
def get_fukushima():
    return fukushima

@router.get('/ibaraki')
def get_ibaraki():
    return ibaraki

@router.get('/tochigi')
def get_tochigi():
    return tochigi

@router.get('/gunma')
def get_gunma():
    return gunma

@router.get('/saitama')
def get_saitama():
    return saitama

@router.get('/chiba')
def get_chiba():
    return chiba

@router.get('/tokyo')
def get_tokyo():
    return tokyo

@router.get('/kanagawa')
def get_kanagawa():
    return kanagawa

@router.get('/niigata')
def get_niigata():
    return niigata

@router.get('/toyama')
def get_toyama():
    return toyama

@router.get('/ishikawa')
def get_ishikawa():
    return ishikawa

@router.get('/fukui')
def get_fukui():
    return fukui

@router.get('/yamanashi')
def get_yamanashi():
    return yamanashi

@router.get('/nagano')
def get_nagano():
    return nagano

@router.get('/gifu')
def get_gifu():
    return gifu

@router.get('/shizuoka')
def get_shizuoka():
    return shizuoka

@router.get('/aichi')
def get_aichi():
    return aichi

@router.get('/mie')
def get_mie():
    return mie

@router.get('/shiga')
def get_shiga():
    return shiga

@router.get('/kyoto')
def get_kyoto():
    return kyoto

@router.get('/osaka')
def get_osaka():
    return osaka

@router.get('/hyogo')
def get_hyogo():
    return hyogo

@router.get('/nara')
def get_nara():
    return nara

@router.get('/wakayama')
def get_wakayama():
    return wakayama

@router.get('/tottori')
def get_tottori():
    return tottori

@router.get('/shimane')
def get_shimane():
    return shimane

@router.get('/okayama')
def get_okayama():
    return okayama

@router.get('/hiroshima')
def get_hiroshima():
    return hiroshima

@router.get('/yamaguchi')
def get_yamaguchi():
    return yamaguchi

@router.get('/tokushima')
def get_tokushima():
    return tokushima

@router.get('/kagawa')

def get_kagawa():
    return kagawa

@router.get('/ehime')
def get_ehime():
    return ehime

@router.get('/kochi')
def get_kochi():
    return kochi

@router.get('/fukuoka')
def get_fukuoka():
    return fukuoka

@router.get('/saga')
def get_saga():
    return saga

@router.get('/nagasaki')
def get_nagasaki():
    return nagasaki

@router.get('/kumamoto')
def get_kumamoto():
    return kumamoto

@router.get('/oita')
def get_oita():
    return oita

@router.get('/miyazaki')
def get_miyazaki():
    return miyazaki

@router.get('/kagoshima')
def get_kagoshima():
    return kagoshima

@router.get('/okinawa')
def get_okinawa():
    return okinawa

@router.get('/all')
def get_all():
    return japan, hokkaido, aomori, iwate, miyagi, akita, yamagata, fukushima,\
    ibaraki, tochigi, gunma, saitama, chiba, tokyo, kanagawa, niigata,\
    toyama, ishikawa, fukui, yamanashi, nagano, gifu, shizuoka, aichi,\
    mie, shiga, kyoto, osaka, hyogo, nara, wakayama, tottori, shimane,\
    okayama, hiroshima, yamaguchi, tokushima, kagawa, ehime, kochi,\
    fukuoka, saga, nagasaki, kumamoto, oita, miyazaki, kagoshima, okinawa

@router.get('/iso_code/{iso}>')
def get_by_iso(iso: int):
    for prefecture in all_prefectures:
        if iso < 1 or iso > 47:
            return 'Enter number between 1-47'
        if iso == prefecture['iso_code']:
            return prefecture

@router.get('/climate/{iso}>')
def get_by_area_rank(iso: int):
    for prefecture in all_prefectures:
        if iso < 1 or iso > 47:
            return 'Enter number between 1-47'
        if iso == prefecture['iso_code']:
            return prefecture['climate']

@router.get('/local_dishes/{iso}>')
def get_by_population_rank(iso: int):
    for prefecture in all_prefectures:
        if iso < 1 or iso > 47:
            return 'Enter number between 1-47'
        if iso == prefecture['iso_code']:
            return prefecture['local_dishes']

@router.get('/area_rank/')
def show_area_rank_message():
    return '<h1>Specify the area rank number 1-47</h1>'

@router.get('/population_rank/')
def show_population_rank_message():
    return '<h1>Specify the population rank number 1-47</h1>'

@router.get('/iso_code/')
def show_iso_code_message():
    return '<h1>Specify the iso code number 1-47</h1>'

@router.get('/random_prefecture')
def get_random_prefecture():
    return random.choice(all_prefectures)

@router.get('/random_fact')
def get_random_fact():
    return {"fact": random.choice(japan_facts)}
