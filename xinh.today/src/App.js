import React, { Component } from 'react'
import StackGrid from "react-stack-grid"
import Lightbox from 'react-images'

const PATH_BASE = 'http://api.xinh.today/images?page='


class App extends Component {
  constructor (props) {
    super(props)

    this.state = {
      data: [],
      isLoading: false,
      nextHref: null,
      lightboxIsOpen: false,
      currentImage: 0
    }
    this.fetchData = this.fetchData.bind(this)
    this.setData = this.setData.bind(this)
    this.fetchNext = this.fetchNext.bind(this)
    this.setRecentHref = this.setRecentHref.bind(this)
    this.scrollToBottom = this.scrollToBottom.bind(this)

    this.closeLightbox = this.closeLightbox.bind(this)
		this.gotoNext = this.gotoNext.bind(this)
		this.gotoPrevious = this.gotoPrevious.bind(this)
		this.gotoImage = this.gotoImage.bind(this)
		this.handleClickImage = this.handleClickImage.bind(this)
		this.openLightbox = this.openLightbox.bind(this)
  }

  openLightbox (index, event) {
		event.preventDefault()
		this.setState({
			currentImage: index,
			lightboxIsOpen: true,
		})
	}

	closeLightbox () {
		this.setState({
			currentImage: 0,
			lightboxIsOpen: false,
		})
	}

	gotoPrevious () {
		this.setState({
			currentImage: this.state.currentImage - 1,
		})
	}

	gotoNext () {
		this.setState({
			currentImage: this.state.currentImage + 1,
		})
	}

	gotoImage (index) {
		this.setState({
			currentImage: index,
		})
	}

	handleClickImage () {
		if (this.state.currentImage === this.props.images.length - 1) return

		this.gotoNext()
	}

  setData (result) {
    const { nextHref } = this.state
    const { results } = result
    const oldData = nextHref ? this.state.data : []
    const updatedData = [...oldData, ...results]
    this.setState({ data: updatedData, nextHref: result.next, isLoading: false })
  }

  setRecentHref (result) {
    const pageNum = parseInt(result.next.match(/\d+/)[0], 10) - 1
    localStorage.setItem('recentHref', PATH_BASE + pageNum)
  }

  fetchData (href) {
    fetch(`${href}`)
    .then(response => response.json())
    .then(result => this.setData(result))
    .catch(e => console.log(e))
  }

  fetchNext (nextHref) {
    this.setState({isLoading: true})
    fetch(`${nextHref}`)
    .then(response => response.json())
    .then(result => (this.setData(result), this.setRecentHref(result)))
    .catch(e => console.log(e))
  }

  componentDidMount () {
    this.fetchData(PATH_BASE + 1)
  }

  scrollToBottom() {
    this.el.scrollIntoView({ behaviour: 'smooth' })
  }

  componentDidUpdate () {
    this.scrollToBottom()
  }

  render() {
    const { data, isLoading, nextHref } = this.state
    const list = (data) || []
    let recentHref = localStorage.getItem('recentHref') || ""
    let images = list.map(
      function(obj) {
        var n = {};
        n.src = obj['url'];
        n.caption = obj['source'];
        return n
      }
    )
    return (
      <div>
        <section className="hero">
          <div className="hero-body">
            <div className="container has-text-centered">
              <h1 className="title">XINH.TODAY</h1>
              <h2 className="subtitle">Tổng hợp ảnh girl xinh Việt Nam. Cập nhập hằng ngày.</h2>
              { recentHref
                ? (
                    <button className="button is-primary" onClick={() => this.fetchData(recentHref)}>
                      Xem tiếp từ trang {recentHref.match(/\d+/)[0]}
                    </button>
                  )
                  : null
                }
            </div>
          </div>
        </section>
        <div className="section">
          <StackGrid
            monitorImagesLoaded
            columnWidth={300}
            duration={600}
            gutterWidth={15}
            gutterHeight={15}
          >
            {
              list.length
                ? list.map(
                    (item, i) => (
                      <Image key={item.id} item={item} onClick={(e) => this.openLightbox(i, e) } />
                    )
                  )
                : null
            }
          </StackGrid>
          <Lightbox
            currentImage={this.state.currentImage}
            images={images}
            isOpen={this.state.lightboxIsOpen}
  					onClickImage={this.handleClickImage}
  					onClickNext={this.gotoNext}
  					onClickPrev={this.gotoPrevious}
  					onClickThumbnail={this.gotoImage}
            onClose={this.closeLightbox}
          />
          {
            nextHref
              ? <LoadMore nextHref={nextHref} onClickNext={() => this.fetchNext(nextHref)} isLoading={isLoading} />
              : null
          }
          <div className="" ref={el => { this.el = el }}></div>
        </div>
      </div>
    )
  }
}


const Image = ({ item, onClick }) =>
<figure className="image">
  <img src={item.url} alt="" onClick={onClick} style={{'width': 300}}/>
</figure>


const LoadMore = ({nextHref, onClickNext, isLoading}) =>
<div className='container has-text-centered' style={{'paddingTop': '20px'}}>
  <div className='columns'>
    <div className='column is-2-desktop is-offset-5-desktop is-8-mobile is-offset-2-mobile'>
      <a
        className={'button ' + (!nextHref ? ' is-disabled' : ' is-focused' + (isLoading ? ' is-loading' : ''))}
        onClick={onClickNext}
      >
      Xem thêm
    </a>
    </div>
  </div>
</div>

export default App
