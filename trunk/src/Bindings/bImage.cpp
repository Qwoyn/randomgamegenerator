#include "bImage.h"

#include "../cTilesetManager.h"
#include "../cGame.h"
#include "bMain.h"

int bImage::countId = 0;

bImage::bImage()
{
    x = 0;
    y = 0;
    w = 0;
    h = 0;
    tile = 0;
    layer = 0;
    id = 0;
    filename = "";
}

bImage::bImage(int x, int y, int w, int h, int drawW, int drawH, int tile, int layer, QString filename)
{
    this->x = x;
    this->y = y;
    this->w = w;
    this->h = h;
    this->drawW = drawW;
    this->drawH = drawH;
    this->layer = layer;
    this->hidden = false;
    id = countId++;
    this->tile = tile;
    this->filename = filename;
    this->isDestroyed = false;

    if(bMain::getGameInstance() == NULL)
        cout << "ERROR! ERROR!" << endl << "ERROR! ERROR!" << endl << "ERROR! ERROR!" << endl;

    bMain::getGameInstance()->mTilesetManager->addImage(this, layer);

    this->tilesetId = bMain::getGameInstance()->mTilesetManager->getTilesetId(filename.toStdString(), w, h);

    //cout << "created image " << id << ":" << filename.toStdString() << endl;
}

bImage::~bImage()
{
    if(!isDestroyed)
        bMain::getGameInstance()->mTilesetManager->removeImage(this, layer);
    //cout << "removed image " << id << ":" << filename.toStdString() << endl;
}

int bImage::getId()
{
    return id;
}

int bImage::getX()
{
    return x;
}

int bImage::getY()
{
    return y;
}

int bImage::getW()
{
    return w;
}

int bImage::getH()
{
    return h;
}

int bImage::getDrawW()
{
    return drawW;
}

int bImage::getDrawH()
{
    return drawH;
}

int bImage::getTile()
{
    return tile;
}

int bImage::getLayer()
{
    return layer;
}

bool bImage::getHidden()
{
    return hidden;
}


QString bImage::getFilename()
{
    return filename;
}

int bImage::getTilesetId()
{
    return tilesetId;
}


int bImage::getTilesetW()
{
    return bMain::getGameInstance()->mTilesetManager->findTileset(tilesetId)->getW();
}

int bImage::getTilesetH()
{
    return bMain::getGameInstance()->mTilesetManager->findTileset(tilesetId)->getH();
}


void bImage::setX(int x)
{
    this->x = x;
}

void bImage::setY(int y)
{
    this->y = y;
}

void bImage::setW(int w)
{
    this->w = w;
}

void bImage::setH(int h)
{
    this->h = h;
}

void bImage::setDrawW(int w)
{
    this->drawW = w;
}

void bImage::setDrawH(int h)
{
    this->drawH = h;
}

void bImage::setTile(int tile)
{
    if(bMain::getGameInstance()->mTilesetManager->changeTileOfImage(this, tile))
        this->tile = tile;
}

void bImage::setLayer(int layer)
{
    if(layer < 0)
        return;

    bMain::getGameInstance()->mTilesetManager->changeLayerOfImage(this, this->layer, layer);
    this->layer = layer;
}

void bImage::setHidden(bool hidden)
{
    this->hidden = hidden;
}


GLuint bImage::getTextureId()
{
    return textureId;
}

void bImage::setTextureId(GLuint textureId)
{
    this->textureId = textureId;
}

QRect bImage::getRect()
{
    return QRect(x, y, w, h);
}

void bImage::DELETEME()
{
    if(!isDestroyed)
    {
        bMain::getGameInstance()->mTilesetManager->removeImage(this, layer);
        isDestroyed = true;
    }
}
