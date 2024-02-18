/** @jsxImportSource @emotion/react */


import { Fragment, useCallback, useContext, useRef } from "react"
import { EventLoopContext, StateContexts } from "/utils/context"
import { Event, getBackendURL, getRefValue, getRefValues, isTrue, refs, set_val } from "/utils/state"
import { Dialog as RadixThemesDialog, Text as RadixThemesText, Theme as RadixThemesTheme } from "@radix-ui/themes"
import env from "/env.json"
import { Avatar, Box, Breadcrumb, BreadcrumbItem, Button, Drawer, DrawerBody, DrawerContent, DrawerHeader, DrawerOverlay, FormControl, Heading, HStack, Input, Menu, MenuButton, MenuDivider, MenuItem, MenuList, Modal, ModalBody, ModalContent, ModalFooter, ModalHeader, ModalOverlay, Text, VStack } from "@chakra-ui/react"
import { CloseIcon, DeleteIcon, HamburgerIcon } from "@chakra-ui/icons"
import { SpinningCircles } from "react-loading-icons"
import "@radix-ui/themes/styles.css"
import theme from "/utils/theme.js"
import NextHead from "next/head"



export function Hamburgericon_c98271a08d187d17b68bd3253ad088ed () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_2905983f8758758258aab6a80fcc9a4c = useCallback((_e) => addEvents([Event("state.state.toggle_drawer", {})], (_e), {}), [addEvents, Event])

  return (
    <Button onClick={on_click_e9416bfe015c0fd3bcfc5ccef2e35037} sx={{"background": "#C70039", "px": "4", "py": "2", "h": "auto", "shadow": "rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;", "color": "#fff", "_hover": {"background": "#4c2db3"}}}>
  {`+ New chat`}
</Button>
  )
}

export function Vstack_0350866e7796ac1875bc06704e94ec67 () {
  const [addEvents, connectError] = useContext(EventLoopContext);
  const state__state = useContext(StateContexts.state__state)


  return (
    <VStack alignItems={`stretch`} sx={{"alignItems": "stretch", "justifyContent": "space-between"}}>
  {state__state.chat_titles.map((chat, index_9a1d5ef446d60768d2d31d08f0a1a150) => (
  <HStack key={index_9a1d5ef446d60768d2d31d08f0a1a150} sx={{"color": "#fff", "cursor": "pointer"}}>
  <Box onClick={(_e) => addEvents([Event("state.state.set_chat", {chat_name:chat})], (_e), {})} sx={{"border": "double 1px transparent;", "borderRadius": "10px;", "backgroundImage": "linear-gradient(#111, #111), radial-gradient(circle at top left, #C70039,#4c2db3);", "backgroundOrigin": "border-box;", "backgroundClip": "padding-box, border-box;", "p": "2", "_hover": {"backgroundImage": "linear-gradient(#111, #111), radial-gradient(circle at top left, #C70039,#6649D8);"}, "color": "#fff8", "flex": "1"}}>
  {chat}
</Box>
  <Box sx={{"border": "double 1px transparent;", "borderRadius": "10px;", "backgroundImage": "linear-gradient(#111, #111), radial-gradient(circle at top left, #C70039,#4c2db3);", "backgroundOrigin": "border-box;", "backgroundClip": "padding-box, border-box;", "p": "2", "_hover": {"backgroundImage": "linear-gradient(#111, #111), radial-gradient(circle at top left, #C70039,#6649D8);"}}}>
  <DeleteIcon onClick={(_e) => addEvents([Event("state.state.delete_chat", {})], (_e), {})} sx={{"fontSize": "md", "color": "#fff8", "_hover": {"color": "#fff"}, "cursor": "pointer", "w": "8"}}/>
</Box>
</HStack>
))}
</VStack>
  )
}

export function Closeicon_11ed883525187cdaad471aef955f22dd () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_2905983f8758758258aab6a80fcc9a4c = useCallback((_e) => addEvents([Event("state.state.toggle_drawer", {})], (_e), {}), [addEvents, Event])

  return (
    <CloseIcon onClick={on_click_2905983f8758758258aab6a80fcc9a4c} sx={{"fontSize": "md", "color": "#fff8", "_hover": {"color": "#fff"}, "cursor": "pointer", "w": "8"}}/>
  )
}

export function Closeicon_c90c6601ae2cde3940fecab2e59b2ad0 () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_e9416bfe015c0fd3bcfc5ccef2e35037 = useCallback((_e) => addEvents([Event("state.state.toggle_modal", {})], (_e), {}), [addEvents, Event])

  return (
    <CloseIcon onClick={on_click_e9416bfe015c0fd3bcfc5ccef2e35037} sx={{"fontSize": "sm", "color": "#fff8", "_hover": {"color": "#fff"}, "cursor": "pointer"}}/>
  )
}

export function Fragment_1762bb90abdb81b879b2a22edbbe01a1 () {
  const [addEvents, connectError] = useContext(EventLoopContext);


  return (
    <Fragment>
  {isTrue(connectError !== null) ? (
  <Fragment>
  <RadixThemesDialog.Root open={connectError !== null}>
  <RadixThemesDialog.Content>
  <RadixThemesDialog.Title>
  {`Connection Error`}
</RadixThemesDialog.Title>
  <RadixThemesText as={`p`}>
  {`Cannot connect to server: `}
  {(connectError !== null) ? connectError.message : ''}
  {`. Check if server is reachable at `}
  {getBackendURL(env.EVENT).href}
</RadixThemesText>
</RadixThemesDialog.Content>
</RadixThemesDialog.Root>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  )
}

export function Button_ef632d83b8d318aaed3f9d0b4d4600c6 () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_65775bd3c3ca6de4793090251b518aa6 = useCallback((_e) => addEvents([Event("state.state.create_chat", {})], (_e), {}), [addEvents, Event])

  return (
    <Button onClick={on_click_65775bd3c3ca6de4793090251b518aa6} sx={{"background": "#5535d4", "boxShadow": "md", "px": "4", "py": "2", "h": "auto", "_hover": {"background": "#4c2db3"}, "shadow": "rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;", "color": "#fff"}}>
  {`Create`}
</Button>
  )
}

export function Box_1814b17ccc133d904756ddae23cea8e0 () {
  const state__state = useContext(StateContexts.state__state)


  return (
    <Box>
  {state__state.chats[state__state.current_chat].map((qa, index_039a3707272eee412616d865b653cc2f) => (
  <Box key={index_039a3707272eee412616d865b653cc2f} sx={{"width": "100%"}}>
  <Box sx={{"textAlign": "left", "paddingTop": "8em"}}>
  <Text sx={{"background": "#222", "border": "1px solid", "borderColor": "#fff3", "shadow": "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)", "marginLeft": "5em", "display": "inline-block", "p": "4", "borderRadius": "xl", "maxW": "30em"}}>
  {qa.answer}
</Text>
</Box>
</Box>
))}
</Box>
  )
}

export function Modal_a5f9b941ad9deaf5670339b14b6480af () {
  const state__state = useContext(StateContexts.state__state)


  return (
    <Modal isOpen={state__state.modal_open}>
  <ModalOverlay>
  <ModalContent sx={{"background": "#222", "color": "#fff"}}>
  <ModalHeader>
  <HStack alignItems={`center`} justifyContent={`space-between`} sx={{"alignItems": "center", "justifyContent": "space-between"}}>
  <Text>
  {`Create new chat`}
</Text>
  <Closeicon_c90c6601ae2cde3940fecab2e59b2ad0/>
</HStack>
</ModalHeader>
  <ModalBody>
  <Input_ab7bcb0ccaff54eb20331ff64b12e24f/>
</ModalBody>
  <ModalFooter>
  <Button_ef632d83b8d318aaed3f9d0b4d4600c6/>
</ModalFooter>
</ModalContent>
</ModalOverlay>
</Modal>
  )
}

export function Formcontrol_b48972261020505866a0e80269cd40ba () {
  const ref_question = useRef(null); refs['ref_question'] = ref_question;
  const state__state = useContext(StateContexts.state__state)


  return (
    <FormControl isDisabled={state__state.processing}>
  <HStack sx={{"alignItems": "center", "justifyContent": "space-between"}}>
  <Input id={`question`} placeholder={`Ask a research question`} ref={ref_question} sx={{"background": "#222", "borderColor": "#fff3", "borderWidth": "1px", "p": "4", "_placeholder": {"color": "#fffa"}, "_hover": {"borderColor": "#C70039"}}}/>
  <Button sx={{"background": "#222", "borderColor": "#fff3", "borderWidth": "1px", "p": "4", "_hover": {"background": "#C70039"}, "shadow": "rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;", "color": "#fff"}} type={`submit`}>
  <Fragment_b63270537008a60ad7c622005e3f02ed/>
</Button>
</HStack>
</FormControl>
  )
}

export function Box_368d7c856fcd75c8256d2c941fb686fc () {
  const [addEvents, connectError] = useContext(EventLoopContext);


  return (
    <Box sx={{"position": "fixed", "top": "240px", "right": "0rem", "width": "700px", "maxHeight": "calc(100vh - 120px)", "overflowY": "auto", "paddingBottom": "1rem", "display": isTrue(state__state.submitted) ? `block` : `none`}}>
  <Box sx={{"backgroundColor": "#222", "color": "#fff", "border": "1px solid", "borderColor": "#fff3", "borderRadius": "var(--chakra-radii-md)", "shadow": "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)", "padding": "16px", "width": "70%", "marginBottom": "12px", "height": "auto"}}>
  <Text sx={{"fontWeight": "bold"}}>
  {`Chart`}
</Text>
  {`Content of the first box`}
</Box>
  <Box sx={{"backgroundColor": "#222", "color": "#fff", "border": "1px solid", "borderColor": "#fff3", "borderRadius": "var(--chakra-radii-md)", "shadow": "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)", "padding": "16px", "width": "70%", "marginBottom": "12px", "height": "auto"}}>
  <Text sx={{"fontWeight": "bold"}}>
  {`Research Gap`}
</Text>
  {`Content of the second box`}
</Box>
</Box>
  )
}

export function Vstack_48cf8d79b2b602d694a649406e7a3f5a () {
  const state__state = useContext(StateContexts.state__state)


  return (
    <VStack sx={{"py": "8", "flex": "1", "width": "100%", "maxW": "3xl", "paddingInlineStart": "4", "paddingInlineEnd": "4", "alignSelf": "center", "overflow": "auto", "paddingBottom": "5em", "display": isTrue(state__state.submitted) ? `block` : `none`, "alignItems": "stretch", "justifyContent": "space-between"}}>
  <Box_1814b17ccc133d904756ddae23cea8e0/>
</VStack>
  )
}

export function Box_6ad5ee50aea838e2e82dd27c5f1a78b2 () {
  const state__state = useContext(StateContexts.state__state)


  return (
    <Box sx={{"position": isTrue(((state__state.submitted) === (true))) ? `fixed` : `absolute`, "top": isTrue(((state__state.submitted) === (true))) ? `0%` : `50%`, "left": isTrue(((state__state.submitted) === (true))) ? `0%` : `50%`, "transform": isTrue(((state__state.submitted) === (true))) ? `` : `translate(-50%, -50%)`, "py": "4", "backdropFilter": "auto", "backdropBlur": "lg", "alignItems": "stretch", "width": "100%"}}>
  <VStack sx={{"width": "100%", "maxW": "3xl", "mx": "auto", "alignItems": "stretch", "justifyContent": "space-between"}}>
  <Text sx={{"fontSize": "3xl", "fontWeight": "bold", "color": "#FFFFFF", "textAlign": "center", "width": "100%", "marginBottom": "2em"}}>
  {`Explore the scientific literature`}
</Text>
  <Box_368d7c856fcd75c8256d2c941fb686fc/>
  <Text sx={{"fontSize": "xs", "color": "#fff6", "textAlign": "center"}}>
  {`Althea is a research assistant. Use with discretion.`}
</Text>
</VStack>
  <Box_620608ac2582bc6eee69f07b8ff2f4a9/>
</Box>
  )
}

export function Button_cab989f12f0ad9235e6312d2dfd88c7b () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_e9416bfe015c0fd3bcfc5ccef2e35037 = useCallback((_e) => addEvents([Event("state.state.toggle_modal", {})], (_e), {}), [addEvents, Event])

  return (
    <Button onClick={on_click_e9416bfe015c0fd3bcfc5ccef2e35037} sx={{"background": "#C70039", "px": "4", "py": "2", "h": "auto", "shadow": "rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;", "color": "#fff", "_hover": {"background": "#4c2db3"}}}>
  {`+ New chat`}
</Button>
  )
}

export function Drawer_97f35b88b43e4dff28cc84b566060908 () {
  const state__state = useContext(StateContexts.state__state)


  return (
    <Drawer isOpen={state__state.drawer_open} placement={`left`}>
  <DrawerOverlay>
  <DrawerContent sx={{"background": "#111", "color": "#fff", "opacity": "0.9"}}>
  <DrawerHeader>
  <HStack sx={{"alignItems": "center", "justifyContent": "space-between"}}>
  <Text>
  {`Research history`}
</Text>
  <Closeicon_11ed883525187cdaad471aef955f22dd/>
</HStack>
</DrawerHeader>
  <DrawerBody>
  <Vstack_0350866e7796ac1875bc06704e94ec67/>
</DrawerBody>
</DrawerContent>
</DrawerOverlay>
</Drawer>
  )
}

export function Box_8a252364875ee458a85364c8c008a516 () {
  
    const handleSubmit_d7cdf26011022355cc967f56c1077705 = useCallback((ev) => {
        const $form = ev.target
        ev.preventDefault()
        const form_data = {...Object.fromEntries(new FormData($form).entries()), ...{"question": getRefValue(refs['ref_question'])}}

        addEvents([Event("state.state.process_question", {form_data:form_data})])

        if (false) {
            $form.reset()
        }
    })
    
  const [addEvents, connectError] = useContext(EventLoopContext);


  return (
    <Box as={`form`} onSubmit={handleSubmit_d7cdf26011022355cc967f56c1077705} sx={{"width": "100%"}}>
  <Formcontrol_b48972261020505866a0e80269cd40ba/>
</Box>
  )
}

export function Box_fdf2bbb54ac5ea3eca7ccea39b2c159b () {
  const state__state = useContext(StateContexts.state__state)


  return (
    <Box sx={{"position": isTrue(((state__state.submitted) === (true))) ? `fixed` : `absolute`, "top": isTrue(((state__state.submitted) === (true))) ? `0%` : `50%`, "left": isTrue(((state__state.submitted) === (true))) ? `0%` : `50%`, "transform": isTrue(((state__state.submitted) === (true))) ? `` : `translate(-50%, -50%)`, "py": "4", "backdropFilter": "auto", "backdropBlur": "lg", "alignItems": "stretch", "width": "100%"}}>
  <VStack sx={{"width": "100%", "maxW": "3xl", "mx": "auto", "alignItems": "stretch", "justifyContent": "space-between"}}>
  <Text sx={{"fontSize": "3xl", "fontWeight": "bold", "color": "#FFFFFF", "textAlign": "center", "width": "100%", "marginBottom": "2em"}}>
  {`Explore the scientific literature`}
</Text>
  <Box_8a252364875ee458a85364c8c008a516/>
  <Text sx={{"fontSize": "xs", "color": "#fff6", "textAlign": "center"}}>
  {`Althea is a research agent. Use discretion.`}
</Text>
</VStack>
</Box>
  )
}

export function Input_ab7bcb0ccaff54eb20331ff64b12e24f () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_blur_655009403944aacdde6d38e4aa5f79da = useCallback((_e0) => addEvents([Event("state.state.set_new_chat_name", {value:_e0.target.value})], (_e0), {}), [addEvents, Event])

  return (
    <Input onBlur={on_blur_655009403944aacdde6d38e4aa5f79da} placeholder={`Type something...`} sx={{"background": "#222", "borderColor": "#fff3", "_placeholder": {"color": "#fffa"}}}/>
  )
}

export function Button_cab989f12f0ad9235e6312d2dfd88c7b () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_e9416bfe015c0fd3bcfc5ccef2e35037 = useCallback((_e) => addEvents([Event("state.state.toggle_modal", {})], (_e), {}), [addEvents, Event])

  return (
    <Button onClick={on_click_e9416bfe015c0fd3bcfc5ccef2e35037} sx={{"background": "#C70039", "px": "4", "py": "2", "h": "auto", "shadow": "rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;", "color": "#fff", "_hover": {"background": "#4c2db3"}}}>
  {`+ New chat`}
</Button>
  )
}

export function Hamburgericon_c98271a08d187d17b68bd3253ad088ed () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_2905983f8758758258aab6a80fcc9a4c = useCallback((_e) => addEvents([Event("state.state.toggle_drawer", {})], (_e), {}), [addEvents, Event])

  return (
    <HamburgerIcon onClick={on_click_2905983f8758758258aab6a80fcc9a4c} sx={{"mr": 4, "cursor": "pointer"}}/>
  )
}

export function Fragment_1762bb90abdb81b879b2a22edbbe01a1 () {
  const [addEvents, connectError] = useContext(EventLoopContext);


  return (
    <Fragment>
  {isTrue(connectError !== null) ? (
  <Fragment>
  <RadixThemesDialog.Root open={connectError !== null}>
  <RadixThemesDialog.Content>
  <RadixThemesDialog.Title>
  {`Connection Error`}
</RadixThemesDialog.Title>
  <RadixThemesText as={`p`}>
  {`Cannot connect to server: `}
  {(connectError !== null) ? connectError.message : ''}
  {`. Check if server is reachable at `}
  {getBackendURL(env.EVENT).href}
</RadixThemesText>
</RadixThemesDialog.Content>
</RadixThemesDialog.Root>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  )
}

export default function Component() {

  return (
    <Fragment>
  <Fragment_1762bb90abdb81b879b2a22edbbe01a1/>
  <VStack alignItems={`stretch`} spacing={`0`} sx={{"background": "#111", "color": "#fff", "minH": "100vh", "alignItems": "stretch", "justifyContent": "space-between"}}>
  <Box sx={{"background": "#111", "backdropFilter": "auto", "backdropBlur": "lg", "p": "4", "borderBottom": "1px solid #fff3", "position": "sticky", "top": "0", "zIndex": "100"}}>
  <HStack justify={`space-between`} sx={{"alignItems": "center", "justifyContent": "space-between"}}>
  <HStack sx={{"alignItems": "center", "justifyContent": "space-between"}}>
  <Hamburgericon_c98271a08d187d17b68bd3253ad088ed/>
  <Breadcrumb>
  <BreadcrumbItem>
  <Heading size={`md`} sx={{"fontWeight": "bold"}}>
  {`Althea`}
</Heading>
</BreadcrumbItem>
</Breadcrumb>
</HStack>
  <HStack spacing={`4`} sx={{"alignItems": "center", "justifyContent": "space-between"}}>
  <Button_cab989f12f0ad9235e6312d2dfd88c7b/>
  <Menu sx={{"background": "#111", "border": "red"}}>
  <MenuButton>
  <Avatar name={`NB`} size={`md`} sx={{"shadow": "rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;", "color": "#fff", "background": "#fff3"}}/>
  <Box/>
</MenuButton>
  <MenuList sx={{"background": "#111", "border": "1.5px solid #222"}}>
  <MenuItem sx={{"background": "#111", "color": "#fff"}}>
  {`Help`}
</MenuItem>
  <MenuDivider sx={{"border": "1px solid #222"}}/>
  <MenuItem sx={{"background": "#111", "color": "#fff"}}>
  {`Settings`}
</MenuItem>
</MenuList>
</Menu>
</HStack>
</HStack>
</Box>
  <Box sx={{"minHeight": "100vh"}}>
  <Box_6ad5ee50aea838e2e82dd27c5f1a78b2/>
  <Box_620608ac2582bc6eee69f07b8ff2f4a9/>
  <Vstack_48cf8d79b2b602d694a649406e7a3f5a/>
</Box>
  <Drawer_97f35b88b43e4dff28cc84b566060908/>
  <Modal_a5f9b941ad9deaf5670339b14b6480af/>
</VStack>
  <NextHead>
  <title>
  {`Reflex App`}
</title>
  <meta content={`A Reflex app.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
